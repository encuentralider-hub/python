from sqlmodel import SQLModel, create_engine, Session

# Nombre del archivo físico que se creará en tu proyecto
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# El argumento check_same_thread=False es necesario en SQLite con FastAPI
# para permitir que múltiples peticiones concurrentes funcionen bien.
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

# Función para crear las tablas al iniciar la app
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Inyección de Dependencia: Generador de Sesiones
def get_session():
    with Session(engine) as session:
        yield session  # Entrega la sesión al endpoint, y cuando el endpoint termina, la cierra automáticamente
