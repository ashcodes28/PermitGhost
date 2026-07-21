from fastapi import FastAPI

from database import Base, engine
from api import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PermitGhost API",
    description="AI-Powered Industrial Safety Intelligence Platform",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to PermitGhost!",
        "status": "Backend Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }