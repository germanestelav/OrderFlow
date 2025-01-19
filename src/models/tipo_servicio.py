from sqlalchemy import Column, Integer, String
from database.db_mysql import Base
from sqlalchemy.orm import relationship

class TipoServicio(Base):
    __tablename__ = "tiposservicios"

    TipoServicioID = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(String(100), nullable=False)
    
    # Relación inversa con clientes
    clientes = relationship("Cliente", back_populates="tiposervicio", cascade="all, delete-orphan")

    def to_dict(self):
        """
        Convierte el modelo a un diccionario para facilitar su uso en JSON.
        """
        return {
            "TipoServicioID": self.TipoServicioID,
            "Nombre": self.Nombre,
        }
