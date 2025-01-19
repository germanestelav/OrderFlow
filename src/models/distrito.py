from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db_mysql import Base

class Distrito(Base):
    __tablename__ = "distritos"

    DistritoID = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(String(100), nullable=False)
    ProvinciaID = Column(Integer, ForeignKey("provincias.ProvinciaID"), nullable=False)

    # Relación con la tabla provincias
    provincia = relationship("Provincia", back_populates="distritos")

    # Relación con Condominios
    condominios = relationship("Condominio", back_populates="distrito")

    # Relación inversa con clientes
    clientes = relationship("Cliente", back_populates="distrito")

    def to_dict(self):
        """
        Convierte el modelo a un diccionario para facilitar su uso en JSON.
        """
        return {
            "DistritoID": self.DistritoID,
            "Nombre": self.Nombre,
            "ProvinciaID": self.ProvinciaID,
            "ProvinciaNombre": self.provincia.Nombre if self.provincia else None,
        }
