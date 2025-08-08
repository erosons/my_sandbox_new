#  Here’s expanded, practical documentation for the Python/FastAPI + DuckDB approach that serves Delta or Iceberg tables directly from Azure Blob Storage (ADLS Gen2).
Overview

    Upstream semantics live in dbt/Databricks (views/models/materializations).

    Storage holds curated Delta/Iceberg gold tables under a container.

    API (FastAPI) uses DuckDB with httpfs + delta/iceberg extensions to read table roots over HTTPS using short-lived SAS.

    Governance remains upstream; the API applies light filtering, pagination/limits, and exposes lineage (snapshot/version).

Identity, Access, and SAS (AAD-first)

    Managed Identity for the app is recommended (App Service, Container Apps, AKS).

    Minimal roles on the storage account or container:

        Storage Blob Data Reader — read data plane.

        Storage Blob Data Contributor — only if the app must write (not needed for read-only).

        Storage Blob Delegator — required if your app creates user delegation SAS (used by this design).

    The API requests a User Delegation Key and mints container-level SAS with Read + List for 5–15 minutes.

        Why List? DuckDB needs to enumerate table files and transaction logs.

        Prefer container-level SAS for simplicity; for tight scoping, generate path-scoped SAS and validate requested paths in the API.

    If you cannot grant Delegator, pre-compute and rotate SAS server-side (e.g., with a secured background job) and load it from Key Vault.

Storage Layout & Table Roots

    Delta: the table root is the folder that contains /_delta_log/.

        Example: gold/curated/customer_360/ → .../customer_360/_delta_log/…

    Iceberg: the table root is the folder that contains /metadata/ (and data/, snapshots/, etc.).

        Example: gold/curated/sales_iceberg/ → .../sales_iceberg/metadata/...

    The API must pass the table root URL (with SAS) to delta_scan() or iceberg_scan().

Time Travel & Reproducibility

    Delta (DuckDB):

        By version: SELECT … FROM delta_scan(?, version => 157);

        By timestamp (when supported): delta_scan(?, timestamp_as_of => TIMESTAMP '2025-08-06 12:00:00');

    Iceberg (DuckDB):

        By snapshot: iceberg_scan(?, snapshot_id => 1234567890);

        By timestamp: iceberg_scan(?, at_timestamp => TIMESTAMP '2025-08-06 12:00:00');

    Expose the chosen version/snapshot in responses (X-Data-Version, X-Iceberg-Snapshot) for auditing and cache keys.

Caching, CDN, and Headers

    Add a CDN (Azure Front Door) in front of the API.

    Emit:

        Cache-Control: public, max-age=300 (tune as needed).

        ETag: <semantic_model_hash>-<delta_version_or_snapshot_id>.

        Optional: Last-Modified based on table snapshot time.

    For highly repeatable slices (e.g., daily or per-tenant extracts), consider pre-materialized NDJSON endpoints and cache them aggressively.

Performance & Scaling

    Partition pruning: push filters that match your table partitions (e.g., WHERE dt >= '2025-08-01').

    Projection pruning: select only required columns.

    Chunked streaming: use the NDJSON route for large results to manage memory and client backpressure.

    Concurrency:

        DuckDB is process-local; run multiple Uvicorn workers (e.g., --workers 4–8) and autoscale pods/instances.

        Keep one DuckDB connection per worker; avoid creating a connection per request.

    Hot paths: precompute per-tenant/per-segment outputs with dbt/Jobs to reduce on-demand scan cost.

    Network: if Storage has private endpoints, ensure the app is VNET-integrated and can resolve the private blob FQDN.

Security Hardening

    Input allowlists: expose only approved tables and columns. Never accept arbitrary path/table inputs.

    SAS lifetime: keep short (5–15 minutes). Rotate User Delegation Key hourly as shown.

    RBAC: scope roles at the container or account minimal boundary; avoid account keys.

    Secrets: store any fallbacks (precreated SAS, config) in Key Vault; use Managed Identity to access.

    Response shaping: redact PII upstream; re-check at the API boundary.

    DoS protection: rate limit by tenant/API key; bound limit and page size.

Observability & Ops

    Log: request ID, tenant, selected snapshot/version, rows returned, duration, and scan bytes (if available).

    Metrics: p50/p95 latency, error rate, cache hit ratio at CDN, SAS issuance failures, and rows scanned vs. returned.

    Tracing: add OpenTelemetry; propagate trace IDs in responses.

    Health: /healthz checks DuckDB extensions loaded and Storage reachability (HEAD on container).

Error Handling

    Map common failures:

        403/AuthorizationFailure: missing Delegator or data-plane role.

        404: table root wrong (no _delta_log/ or metadata/), or SAS expired.

        416/Range not used here (JSON responses), but be explicit that large downloads use NDJSON streaming.

    Return structured JSON errors with a correlation ID; avoid leaking internal paths.

Local Development

    Auth: use AzureCliCredential or VisualStudioCodeCredential.

    Storage: a dev container (e.g., gold-dev) with sample Delta/Iceberg tables.

    Toggle DEV vs PROD via env:

        STORAGE_ACCOUNT, GOLD_CONTAINER, PORT

        AZURE_CLIENT_ID (if using a user-assigned identity locally)

    Use uvicorn app:app --reload and a small dataset to iterate quickly.

Production Checklist

Managed Identity assigned; roles: Blob Data Reader (+ Delegator if minting SAS).

Private Endpoint + VNET integration (or locked-down firewall + trusted services).

DuckDB extensions installed at boot: httpfs, delta, iceberg.

SAS TTL ≤ 15 minutes; UDK rotated hourly; clock skew handled.

Input validation and strict allowlist for tables/columns.

CDN enabled; ETag includes semantic model + snapshot/version.

FastAPI rate limiting and request/response size limits.

Uvicorn workers sized for CPU/IO; autoscaling in place.

Dashboards for latency, error rate, and SAS issuance success.

    Runbooks for Storage outage, SAS failures, and version pinning rollback.

Gotchas & Tips

    List permission is required: the scan needs to enumerate files under the table root.

    Delta protocol: keep _delta_log/ compact (optimize/vacuum upstream) to reduce metadata overhead.

    Iceberg catalogs: if you use a REST/Nessie/Glue catalog, prefer querying via a service (Databricks SQL/Trino) or ensure your scans operate from table roots with consistent metadata/.

    Schema drift: lock schemas in dbt; expose a model version header; fail fast if columns are missing.

    Large responses: prefer NDJSON streaming and pagination tokens over giant arrays.

If you want, I can fold these into a README.md for your repo and include sample az role assignment commands and a Front Door caching policy snippet.