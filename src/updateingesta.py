from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from sqlmodel import Session, select
from src.models import Email
from src.dependencias import create_db_and_tables, get_session

app = FastAPI()

# Esto asegura que la base de datos se cree en cuanto levantes el servidor
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# El esquema del Día 1: Estricto para validar lo que entra
class EmailIngestSchema(BaseModel):
    sender: EmailStr
    subject: str
    body: str
    category_id: Optional[int] = None

# El nuevo Endpoint conectado a la Base de Datos
@app.post("/emails/", response_model=Email)
def ingest_email(
    email_in: EmailIngestSchema, 
    session: Session = Depends(get_session) # ¡Aquí ocurre la magia de Depends!
):
    # 1. Transformamos el esquema validado en un objeto de la base de datos
    db_email = Email(
        sender=email_in.sender,
        subject=email_in.subject,
        body=email_in.body,
        category_id=email_in.category_id
    )
    
    # 2. Añadimos el objeto al "borrador" de la sesión
    session.add(db_email)
    
    # 3. Guardamos los cambios de forma permanente en SQLite
    session.commit()
    
    # 4. Refrescamos el objeto para obtener el 'id' que SQLite le asignó automáticamente
    session.refresh(db_email)
    
    # Retornamos el registro ya guardado
    return db_email

# ==========================================
# 1. GET: Obtener TODOS los correos
# ==========================================
@app.get("/emails/", response_model=list[Email])
def get_all_emails(session: Session = Depends(get_session)):
    # select(Email) le dice al ORM que genere un "SELECT * FROM email"
    # session.exec() lo ejecuta y .all() nos trae todos los registros en una lista
    correos = session.exec(select(Email)).all()
    return correos

# ==========================================
# 2. GET: Obtener UN SOLO correo por su ID
# ==========================================
@app.get("/emails/{email_id}", response_model=Email)
def get_email(email_id: int, session: Session = Depends(get_session)):
    # session.get() es la forma más rápida de buscar por Primary Key
    correo = session.get(Email, email_id)
    
    if not correo:
        raise HTTPException(status_code=404, detail="Correo no encontrado")
        
    return correo
