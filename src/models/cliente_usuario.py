from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.db_mysql import Base

class ClienteUsuario(Base):
    __tablename__ = 'clientesusuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    UsuarioID = Column(Integer, ForeignKey('usuarios.UsuarioID'), nullable=False)
    ClienteID = Column(Integer, ForeignKey('clientes.ClienteID'), nullable=False)

    # Relaciones
    usuario = relationship("Usuario", back_populates="clientes")
    cliente = relationship("Cliente", back_populates="usuarios")

    def to_dict(self):
        """
        Convierte el modelo a un diccionario para facilitar su uso en JSON.
        """
        return {
            "id": self.id,
            "UsuarioID": self.UsuarioID,
            "ClienteID": self.ClienteID,
        }
