# app/main.py
from fastapi import FastAPI
from app.api.v1.router import api_router

app = FastAPI(
    title="Enterprise Email Ingestion API",
    version="1.0.0"
)

# Conectamos todos los routers de la v1 a la app principal
app.include_router(api_router, prefix="/api/v1")