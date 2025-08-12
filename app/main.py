from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.config import create_tables

@asynccontextmanager
async def lifespan(app: Fastapi):
    await create_tables()
    yield

app = FastAPI(lifespan=lifespan)
