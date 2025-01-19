from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db_mysql import Base

class Provincia(Base):
    __tablename__ = "provincias"

    ProvinciaID = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(String(100), nullable=False)
    DepartamentoID = Column(Integer, ForeignKey("departamentos.DepartamentoID"), nullable=False)

    # Relación con la tabla departamentos
    departamento = relationship("Departamento", back_populates="provincias")

    # Relación con la tabla distritos
    distritos = relationship("Distrito", back_populates="provincia")

    # Relación inversa con clientes
    clientes = relationship("Cliente", back_populates="provincia")

    def to_dict(self):
        """
        Convierte el modelo a un diccionario para facilitar su uso en JSON.
        """
        return {
            "ProvinciaID": self.ProvinciaID,
            "Nombre": self.Nombre,
            "DepartamentoID": self.DepartamentoID,
            "DepartamentoNombre": self.departamento.Nombre if self.departamento else None,
        }
