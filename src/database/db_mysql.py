from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config

# Configuración de la conexión a la base de datos
DATABASE_URL = f"mysql+pymysql://{config('root')}:{config('root')}@{config('localhost')}/{config('gpon')}"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True)

# Configurar la zona horaria al conectarse
@event.listens_for(Engine, "connect")
def set_time_zone(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("SET time_zone = '-05:00';")  # Cambia '-05:00' por tu zona horaria real
    cursor.close()

# Crear una clase base para mapear los modelos
Base = declarative_base()

# Crear la fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
