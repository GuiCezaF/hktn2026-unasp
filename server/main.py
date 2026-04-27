import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Load .env before importing routes that read services (e.g. Twilio).
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

from server.infrastructure.api.routes.api import router

app = FastAPI(title="Incident Response Hub", version="1.0.0")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "dados")

app.mount("/dados", StaticFiles(directory=DATA_DIR), name="dados")

app.include_router(router)
