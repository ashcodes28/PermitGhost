from contextlib import asynccontextmanager
import threading

from fastapi import FastAPI

from database import Base, engine
from api import router
from digital_twin import run_simulation

# Create database tables
Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start Digital Twin in the background
    simulation_thread = threading.Thread(
        target=run_simulation,
        daemon=True
    )
    simulation_thread.start()

    yield


app = FastAPI(
    title="PermitGhost API",
    description="AI-Powered Industrial Safety Intelligence Platform",
    version="1.0.0",
    lifespan=lifespan
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