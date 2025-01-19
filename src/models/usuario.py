from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database.db_mysql import Base
import enum


# Definición del estado como Enum
class EstadoEnum(enum.Enum):
    activo = "activo"
    inactivo = "inactivo"

class Usuario(Base):
    __tablename__ = "usuarios"

    UsuarioID = Column(Integer, primary_key=True, autoincrement=True)
    NombreUsuario = Column(String(50), nullable=False)
    Contrasena = Column(String(255), nullable=False)
    Nombres = Column(String(100), nullable=False)
    Apellidos = Column(String(100), nullable=False)
    TipoDocumento = Column(String(20), nullable=False)
    NumeroIdentificacion = Column(String(20), nullable=False)
    Estado = Column(Enum(EstadoEnum), default=EstadoEnum.activo, nullable=False)
    Email = Column(String(100), nullable=False)
    DepartamentoID = Column(Integer, ForeignKey("departamentos.DepartamentoID"), nullable=True)

    # Relación con departamentos
    departamento = relationship("Departamento", back_populates="usuarios")

    roles = relationship("UsuarioRol", back_populates="usuario", cascade="all, delete-orphan")

    clientesusuarios = relationship("ClienteUsuario", back_populates="usuario", cascade="all, delete-orphan")

    # Relación con ClienteUsuario
    clientes = relationship("ClienteUsuario", back_populates="usuario")

    # Relación con comentariosclientes
    comentarios = relationship("ComentarioCliente", back_populates="usuario")

    def to_dict(self):
        """
        Convierte el modelo a un diccionario para facilitar su uso en JSON.
        """
        return {
            "UsuarioID": self.UsuarioID,
            "NombreUsuario": self.NombreUsuario,
            "Nombres": self.Nombres,
            "Apellidos": self.Apellidos,
            "TipoDocumento": self.TipoDocumento,
            "NumeroIdentificacion": self.NumeroIdentificacion,
            "Estado": self.Estado.value,
            "Email": self.Email,
            "DepartamentoID": self.DepartamentoID,
            "DepartamentoNombre": self.departamento.Nombre if self.departamento else None,
        }
