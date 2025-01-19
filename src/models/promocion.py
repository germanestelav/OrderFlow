from sqlalchemy import Column, Integer, String, Date, Enum
from sqlalchemy.orm import relationship
from database.db_mysql import Base
import enum

class EstadoEnum(enum.Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"

class Promocion(Base):
    __tablename__ = "promociones"

    PromoID = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(String(100), nullable=False)
    FechaInicio = Column(Date, nullable=True)
    FechaFin = Column(Date, nullable=True)
    Estado = Column(Enum(EstadoEnum), default=EstadoEnum.Inactivo, nullable=False)

    # Relación con clientes
    clientes = relationship("Cliente", back_populates="promocion")
    
    def to_dict(self):
        """
        Convierte el modelo a un diccionario para facilitar su uso en JSON.
        """
        return {
            "PromoID": self.PromoID,
            "Nombre": self.Nombre,
            "FechaInicio": str(self.FechaInicio) if self.FechaInicio else None,
            "FechaFin": str(self.FechaFin) if self.FechaFin else None,
            "Estado": self.Estado.value,
        }
