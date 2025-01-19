from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database.db_mysql import Base

class UsuarioRol(Base):
    __tablename__ = "usuariosroles"

    usuariosroles_id = Column(Integer, primary_key=True, autoincrement=True)
    UsuarioID = Column(Integer, ForeignKey("usuarios.UsuarioID"), nullable=False)
    RolID = Column(Integer, ForeignKey("roles.RolID"), nullable=False)
    estado = Column(Boolean, default=True, nullable=False)

    # Relaciones con la tabla usuario
    usuario = relationship("Usuario", back_populates="roles")

    # Relaciones con la tabla roles
    rol = relationship("Rol", back_populates="usuarios")

    def to_dict(self):
        """
        Convierte el modelo a un diccionario para facilitar su uso en JSON.
        """
        return {
            "usuariosroles_id": self.usuariosroles_id,
            "UsuarioID": self.UsuarioID,
            "RolID": self.RolID,
            "estado": self.estado,
            "UsuarioNombre": self.usuario.NombreUsuario if self.usuario else None,
            "RolNombre": self.rol.NombreRol if self.rol else None,
        }
