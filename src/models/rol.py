from sqlalchemy import Column, Integer, String
from database.db_mysql import Base

class Rol(Base):
    __tablename__ = "roles"

    RolID = Column(Integer, primary_key=True, autoincrement=True)
    NombreRol = Column(String(50), nullable=False)

    def to_dict(self):
        """
        Convierte el modelo a un diccionario para facilitar su uso en JSON.
        """
        return {
            "RolID": self.RolID,
            "NombreRol": self.NombreRol,
        }
