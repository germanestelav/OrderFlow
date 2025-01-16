from sqlalchemy import Column, Integer, String
from database.db_mysql import Base

class Area(Base):
    __tablename__ = "areas"  # Nombre de la tabla en la base de datos

    AreaID = Column(Integer, primary_key=True, autoincrement=True)  # Clave primaria
    Nombre = Column(String(100), nullable=False)  # Nombre del área (obligatorio)

    def __repr__(self):
        return f"<Area(AreaID={self.AreaID}, Nombre='{self.Nombre}')>"
