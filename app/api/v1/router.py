# app/api/v1/router.py
from fastapi import APIRouter
from app.api.v1.endpoints import emails

api_router = APIRouter()

# Conectamos el router de emails bajo el prefijo /emails
api_router.include_router(emails.router, prefix="/emails", tags=["Emails"])