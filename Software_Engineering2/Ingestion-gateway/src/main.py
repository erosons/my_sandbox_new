from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession
from auth.jwt import verify_jwt
from db.models import Record
from db.session import get_session
from schemas import RecordIn, RecordOut

app = FastAPI(title="Ingestion Gateway")

auth_scheme = HTTPBearer()

@app.post("/ingest", response_model=RecordOut)
async def ingest(record: RecordIn,
                 token=Depends(auth_scheme),
                 session: AsyncSession = Depends(get_session)):
    verify_jwt(token.credentials)          # raises HTTPException on failure
    db_item = Record(**record.dict())
    session.add(db_item)
    await session.commit()
    await session.refresh(db_item)
    return db_item
