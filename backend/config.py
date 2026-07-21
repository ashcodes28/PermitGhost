from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATABASE_URL = f"sqlite:///{BASE_DIR / 'permitghost.db'}"

PROJECT_NAME = "PermitGhost"

API_VERSION = "v1"

SIMULATION_INTERVAL = 1

RAG_PATH = BASE_DIR.parent / "data"

MODEL_NAME = "all-MiniLM-L6-v2"