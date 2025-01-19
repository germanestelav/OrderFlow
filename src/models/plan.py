from sqlalchemy import Column, Integer, String, Date, Enum
from database.db_mysql import Base
from sqlalchemy.orm import relationship
import enum

# Define los posibles valores del ENUM
class EstadoEnum(enum.Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"

class Plan(Base):
    __tablename__ = 'planes'  # Nombre de la tabla en la base de datos

    PlanID = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(String(100), nullable=False)
    FechaInicio = Column(Date, nullable=True)  # Puede ser nulo
    FechaFin = Column(Date, nullable=True)  # Puede ser nulo
    Estado = Column(Enum(EstadoEnum), nullable=False, default=EstadoEnum.Inactivo)

    # Relación con la tabla clientes
    clientes = relationship("Cliente", back_populates="plan")

    def to_dict(self):
        """
        Convierte el modelo a un diccionario para facilitar su uso en JSON.
        """
        return {
            "PlanID": self.PlanID,
            "Nombre": self.Nombre,
            "FechaInicio": str(self.FechaInicio) if self.FechaInicio else None,
            "FechaFin": str(self.FechaFin) if self.FechaFin else None,
            "Estado": self.Estado.value,
        }
