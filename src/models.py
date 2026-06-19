from typing import Optional
from sqlmodel import Field, SQLModel

# 1. Tabla de Categorías (Support, Billing, Spam, etc.)
class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)

# 2. Tabla de Correos
class Email(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sender: str
    subject: str
    body: str
    
    # Llave foránea para relacionar el correo con una categoría
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")

