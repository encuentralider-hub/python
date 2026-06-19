# app/api/v1/endpoints/emails.py
from fastapi import APIRouter, HTTPException
from typing import Dict
from app.models.schemas import EmailIngestSchema

# Creamos el enrutador específico para este dominio
router = APIRouter()

# Base de datos simulada (temporalmente vive aquí)
email_db: Dict[int, dict] = {}
current_id = 1

@router.post("/ingest", status_code=201)
async def ingest_email(email: EmailIngestSchema):
    global current_id
    email_db[current_id] = email.model_dump()
    assigned_id = current_id
    current_id += 1
    return {"message": "Correo procesado", "id": assigned_id, "data": email_db[assigned_id]}

@router.get("/{email_id}")
async def get_email(email_id: int):
    if email_id not in email_db:
        raise HTTPException(status_code=404, detail="Correo no encontrado")
    return email_db[email_id]

@router.put("/{email_id}")
async def update_email(email_id: int, email: EmailIngestSchema):
    if email_id not in email_db:
        raise HTTPException(status_code=404, detail="Correo no encontrado")
    email_db[email_id] = email.model_dump()
    return {"message": "Correo actualizado", "data": email_db[email_id]}

@router.delete("/{email_id}")
async def delete_email(email_id: int):
    if email_id not in email_db:
        raise HTTPException(status_code=404, detail="Correo no encontrado")
    del email_db[email_id]
    return {"message": f"Correo {email_id} eliminado exitosamente"}