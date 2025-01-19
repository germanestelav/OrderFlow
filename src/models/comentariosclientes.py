from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from database.db_mysql import Base
from sqlalchemy.sql import func

class ComentarioCliente(Base):
    __tablename__ = "comentariosclientes"

    ComentarioID = Column(Integer, primary_key=True, autoincrement=True)
    ClienteID = Column(Integer, ForeignKey("clientes.ClienteID"), nullable=False)
    UsuarioID = Column(Integer, ForeignKey("usuarios.UsuarioID"), nullable=False)
    Comentario = Column(String(255), nullable=False)
    FechaHora = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(),  # Esto asegura que se actualice automáticamente
        nullable=False
    )

    # Relaciones
    cliente = relationship("Cliente", back_populates="comentarios")
    usuario = relationship("Usuario", back_populates="comentarios")

    def to_dict(self):
        return {
            "ComentarioID": self.ComentarioID,
            "ClienteID": self.ClienteID,
            "UsuarioID": self.UsuarioID,
            "Comentario": self.Comentario,
            "FechaHora": self.FechaHora.isoformat() if self.FechaHora else None
        }
