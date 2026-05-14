from fastapi import FastAPI
from contextlib import asynccontextmanager
from routes_a import router
from routes_b import router as router_b
from database import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title="Zadaća 2 - REST API",
    version="1.0.0",
    lifespan=lifespan
)


app.include_router(router)
app.include_router(router_b)


@app.get("/")
def read_root():
    return {"message": "Zadaća 2 - REST API"}