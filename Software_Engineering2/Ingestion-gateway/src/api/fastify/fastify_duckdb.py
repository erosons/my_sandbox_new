# requirements:
#   fastapi uvicorn duckdb azure-identity azure-storage-blob
# run:
#   uvicorn app:app --host 0.0.0.0 --port 8000

import os
import time
import duckdb
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse, StreamingResponse
from azure.identity import DefaultAzureCredential
from azure.storage.blob import (
    BlobServiceClient,
    generate_container_sas,
    ContainerSasPermissions,
)

APP_PORT = int(os.getenv("PORT", "8000"))
ACCOUNT_NAME = os.environ["STORAGE_ACCOUNT"]           # e.g., "mystorageacct"
CONTAINER = os.getenv("GOLD_CONTAINER", "gold")        # e.g., "gold"

# ---- DuckDB: load HTTP + Delta/Iceberg extensions
con = duckdb.connect(":memory:")
for ext in ("httpfs", "delta", "iceberg"):
    con.execute(f"INSTALL {ext};")
    con.execute(f"LOAD {ext};")

# ---- Azure: Blob client + cached User Delegation Key for SAS
credential = DefaultAzureCredential()
bsc = BlobServiceClient(f"https://{ACCOUNT_NAME}.blob.core.windows.net", credential=credential)
_udk = {"key": None, "exp": 0}

def _container_sas(minutes: int = 10) -> str:
    now = int(time.time())
    if _udk["key"] is None or now > _udk["exp"] - 60:
        start = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now - 60))
        end = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now + 3600))
        udk = bsc.get_user_delegation_key(starts_on=start, expires_on=end)
        _udk["key"], _udk["exp"] = udk, now + 3600
    sas = generate_container_sas(
        account_name=ACCOUNT_NAME,
        container_name=CONTAINER,
        user_delegation_key=_udk["key"],
        permission=ContainerSasPermissions(read=True, list=True),
        expiry=time.gmtime(now + minutes * 60),
    )
    return sas

def _table_url(prefix: str, sas: str) -> str:
    # prefix is the folder (table root) ending with '/', containing _delta_log/ (Delta)
    # or metadata/ (Iceberg)
    base = f"https://{ACCOUNT_NAME}.blob.core.windows.net/{CONTAINER}/{prefix}"
    return f"{base}?{sas}"

app = FastAPI(title="Storage-native Semantic API (Delta/Iceberg)")

# ---------- Delta example ----------
@app.get("/delta/customer-360")
def customer_360(
    since: str = Query("2024-01-01"),
    limit: int = Query(100, ge=1, le=10000),
):
    try:
        sas = _container_sas(minutes=10)
        # Path to Delta table root (folder with _delta_log/)
        table_root = "curated/customer_360/"
        delta_url = _table_url(table_root, sas)

        sql = """
            SELECT customer_id, name, recency_score, lifetime_value, segment
            FROM delta_scan(?)
            WHERE signup_date >= ?
            ORDER BY recency_score DESC
            LIMIT ?
        """
        df = con.execute(sql, [delta_url, since, limit]).fetch_df()
        # Optional: stream as NDJSON for huge results; here we return JSON.
        return JSONResponse(df.to_dict(orient="records"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Streaming NDJSON variant (useful for large results)
@app.get("/delta/customer-360.ndjson")
def customer_360_ndjson(
    since: str = Query("2024-01-01"),
    limit: int = Query(1000, ge=1, le=1_000_000),
):
    try:
        import json
        sas = _container_sas(minutes=10)
        table_root = "curated/customer_360/"
        delta_url = _table_url(table_root, sas)
        sql = """
            SELECT customer_id, name, recency_score, lifetime_value, segment
            FROM delta_scan(?)
            WHERE signup_date >= ?
            ORDER BY recency_score DESC
            LIMIT ?
        """
        # Use DuckDB's streaming via chunks
        def gen():
            con.execute(sql, [delta_url, since, limit])
            while True:
                batch = con.fetch_df_chunk()
                if batch is None or batch.empty:
                    break
                for _, row in batch.iterrows():
                    yield json.dumps(row.to_dict()) + "\n"
        return StreamingResponse(gen(), media_type="application/x-ndjson")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ---------- Iceberg example ----------
@app.get("/iceberg/sales-by-region")
def sales_by_region(
    since: str = Query("2024-01-01"),
    limit: int = Query(100, ge=1, le=10000),
):
    try:
        sas = _container_sas(minutes=10)
        # Path to Iceberg table root (folder with metadata/, data/, etc.)
        table_root = "curated/sales_iceberg/"
        iceberg_url = _table_url(table_root, sas)

        sql = """
            SELECT region, SUM(net_sales) AS net_sales
            FROM iceberg_scan(?)
            WHERE order_date >= ?
            GROUP BY 1
            ORDER BY 2 DESC
            LIMIT ?
        """
        df = con.execute(sql, [iceberg_url, since, limit]).fetch_df()
        return JSONResponse(df.to_dict(orient="records"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
