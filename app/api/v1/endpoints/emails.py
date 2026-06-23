# app/api/v1/endpoints/emails.py
from fastapi import APIRouter, HTTPException, Query
from typing import Dict, List, Optional
from app.models.schemas import EmailIngestSchema, EmailStatusUpdate, EmailStatus

router = APIRouter()

# Base de datos simulada
email_db: Dict[int, dict] = {}
current_id = 1

# ... [Aquí iría tu POST /ingest anterior] ...

# 1. GET con Filtros Avanzados y Paginación
@router.get("/")
async def list_emails(
    skip: int = Query(0, ge=0, description="Cuántos correos saltar (Offset)"),
    limit: int = Query(10, le=100, description="Límite de resultados por página"),
    sender: Optional[str] = Query(None, description="Filtrar por remitente exacto"),
    unread_only: bool = Query(False, description="Mostrar solo correos no leídos"),
    search_subject: Optional[str] = Query(None, description="Buscar palabra clave en el asunto")
):
    # Paso 1: Filtrar la información (Simulando el WHERE de SQLModel)
    filtered_emails = []
    
    for email_id, email_data in email_db.items():
        # Si el usuario envió un remitente y no coincide, saltamos este correo
        if sender and email_data["sender"] != sender:
            continue
            
        # Si pidió solo no leídos y este está leído/archivado, lo saltamos
        if unread_only and email_data["status"] != EmailStatus.unread:
            continue
            
        # Si busca una palabra en el asunto, comparamos en minúsculas
        if search_subject and search_subject.lower() not in email_data["subject"].lower():
            continue
            
        # Si sobrevive a los filtros, lo añadimos a nuestra lista temporal
        filtered_emails.append({"id": email_id, **email_data})

    # Paso 2: Aplicar Paginación con Python (Simulando OFFSET y LIMIT de SQL)
    # Usamos "slicing" de listas en Python: lista[inicio:fin]
    paginated_emails = filtered_emails[skip : skip + limit]

    return {
        "total_filtered": len(filtered_emails),
        "skip": skip,
        "limit": limit,
        "data": paginated_emails
    }

# 2. PATCH para actualización parcial
@router.patch("/{email_id}/status")
async def update_email_status(email_id: int, status_update: EmailStatusUpdate):
    if email_id not in email_db:
        raise HTTPException(status_code=404, detail="Correo no encontrado")
    
    # Actualización Quirúrgica: Solo modificamos la llave 'status'. 
    # El resto del correo queda intacto.
    email_db[email_id]["status"] = status_update.status
    
    return {
        "message": "Estado actualizado correctamente",
        "data": {
            "id": email_id, 
            "new_status": email_db[email_id]["status"]
        }
    }