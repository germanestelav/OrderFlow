from sqlalchemy import Column, Integer, String
from database.db_mysql import Base

class EstadoCliente(Base):
    __tablename__ = 'estadoscliente'  # Nombre de la tabla en la base de datos

    EstadoID = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(String(100), nullable=False)

    def to_dict(self):
        """
        Convierte el modelo a un diccionario para facilitar su uso en JSON.
        """
        return {
            "EstadoID": self.EstadoID,
            "Nombre": self.Nombre,
        }
