from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Dict, Optional


# Inicializamos la aplicación FastAPI
app = FastAPI(
    title="Email Ingestion API",
    description="API para procesar y gestionar webhooks de correos electrónicos."
)

# Simulamos una base de datos en memoria usando un diccionario
# Esto preparará el terreno para una integración futura con una base de datos real
email_db: Dict[int, dict] = {}
current_id = 1

# Definición del modelo estricto de Pydantic
class EmailIngestSchema(BaseModel):
    sender: EmailStr
    recipient: EmailStr
    subject: str
    body: str
    timestamp: datetime

# POST: Ingestar un nuevo correo
@app.post("/emails/ingest", status_code=201)
async def ingest_email(email: EmailIngestSchema):
    global current_id
    email_db[current_id] = email.model_dump()
    assigned_id = current_id
    current_id += 1
    return {"message": "Correo procesado con éxito", "id": assigned_id, "data": email_db[assigned_id]}

# GET: Recuperar un correo específico
@app.get("/emails/{email_id}")
async def get_email(email_id: int):
    if email_id not in email_db:
        raise HTTPException(status_code=404, detail="Correo no encontrado")
    return email_db[email_id]

# PUT: Actualizar un correo existente por completo
@app.put("/emails/{email_id}")
async def update_email(email_id: int, email: EmailIngestSchema):
    if email_id not in email_db:
        raise HTTPException(status_code=404, detail="Correo no encontrado")
    
    email_db[email_id] = email.model_dump()
    return {"message": "Correo actualizado", "data": email_db[email_id]}

# DELETE: Eliminar un correo
@app.delete("/emails/{email_id}")
async def delete_email(email_id: int):
    if email_id not in email_db:
        raise HTTPException(status_code=404, detail="Correo no encontrado")
    
    del email_db[email_id]
    return {"message": f"Correo {email_id} eliminado exitosamente"}