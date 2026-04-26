import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

# Load environment variables FIRST
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

from server.infrastructure.api.routes.api import router

app = FastAPI(title="Incident Response Hub", version="1.0.0")

# Setup paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "dados")

# Serve static files from the 'dados' directory
app.mount("/dados", StaticFiles(directory=DATA_DIR), name="dados")

# Include API routes
app.include_router(router)
