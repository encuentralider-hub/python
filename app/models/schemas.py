# app/models/schemas.py
from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum

# Definimos los estados válidos
class EmailStatus(str, Enum):
    unread = "unread"
    read = "read"
    archived = "archived"

# Actualizamos el esquema base
class EmailIngestSchema(BaseModel):
    sender: EmailStr
    recipient: EmailStr
    subject: str
    body: str
    timestamp: datetime
    status: EmailStatus = EmailStatus.unread # Por defecto es 'unread'

# NUEVO: Modelo estricto para el PATCH (Solo permite enviar el estado)
class EmailStatusUpdate(BaseModel):
    status: EmailStatus