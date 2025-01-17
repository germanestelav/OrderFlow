from sqlalchemy import Column, Integer, String
from database.db_mysql import Base

class Departamento(Base):
    __tablename__ = 'departamentos'  # Nombre de la tabla en la base de datos

    DepartamentoID = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(String(100), nullable=False)

    def to_dict(self):
        """
        Convierte el modelo a un diccionario para facilitar su uso en JSON.
        """
        return {
            "DepartamentoID": self.DepartamentoID,
            "Nombre": self.Nombre,
        }
