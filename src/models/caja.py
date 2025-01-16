from sqlalchemy import Column, Integer, String, Numeric
from database.db_mysql import Base


class Caja(Base):
    __tablename__ = 'cajas' # Nombre de la tabla en la base de datos
    cajaID = Column(Integer, primary_key=True)
    codigo = Column(String(50), unique=True, nullable=False)
    latitud = Column(Numeric(10, 8), nullable=False)  # Mayor precisión
    longitud = Column(Numeric(11, 8), nullable=False)  # Mayor precisión

    def to_dict(self):
        """
        Convierte el modelo a un diccionario para facilitar su uso en JSON.
        """
        return {
            "cajaID": self.cajaID,
            "codigo": self.codigo,
            "latitud": float(self.latitud) if self.latitud is not None else None,
            "longitud": float(self.longitud) if self.longitud is not None else None,
        }