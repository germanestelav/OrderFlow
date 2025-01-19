from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db_mysql import Base

class Condominio(Base):
    __tablename__ = "condominios"

    CondominioID = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(String(100), nullable=False)
    DistritoID = Column(Integer, ForeignKey("distritos.DistritoID"), nullable=False)

    # Relación con la tabla distritos
    distrito = relationship("Distrito", back_populates="condominios")

    # Relación con tabla clientes
    clientes = relationship("Cliente", back_populates="condominio")

    def to_dict(self):
        """
        Convierte el modelo a un diccionario para facilitar su uso en JSON.
        """
        return {
            "CondominioID": self.CondominioID,
            "Nombre": self.Nombre,
            "DistritoID": self.DistritoID,
            "DistritoNombre": self.distrito.Nombre if self.distrito else None,  # Incluye el nombre del distrito relacionado
        }
