# app/models/schemas.py
from pydantic import BaseModel, EmailStr
from datetime import datetime

# Definición del modelo estricto de Pydantic
class EmailIngestSchema(BaseModel):
    sender: EmailStr
    recipient: EmailStr
    subject: str
    body: str
    timestamp: datetime