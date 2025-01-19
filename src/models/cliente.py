from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum, TIMESTAMP
from sqlalchemy.orm import relationship
from database.db_mysql import Base
from sqlalchemy.orm import validates

class Cliente(Base):
    __tablename__ = "clientes"

    ClienteID = Column(Integer, primary_key=True, autoincrement=True)
    NumeroIdentificacion = Column(String(20), nullable=False, unique=True)
    TipoDocumento = Column(String(20), nullable=False)
    NombreCompleto = Column(String(100), nullable=False)
    Direccion = Column(String(200), nullable=False)
    DepartamentoID = Column(Integer, ForeignKey("departamentos.DepartamentoID"))
    ProvinciaID = Column(Integer, ForeignKey("provincias.ProvinciaID"))
    DistritoID = Column(Integer, ForeignKey("distritos.DistritoID"))
    CoordenadasGPS = Column(String(50), nullable=True)
    Telefono = Column(String(20), nullable=True)
    Correo = Column(String(100), nullable=True)
    RecomendadoPor = Column(String(100), nullable=True)
    NombreRecomendado = Column(String(100), nullable=True)
    TipoServicioID = Column(Integer, ForeignKey("tiposservicios.TipoServicioID"), nullable=True)
    PlanID = Column(Integer, ForeignKey("planes.PlanID"))
    PromoID = Column(Integer, ForeignKey("promociones.PromoID"))
    Fecha = Column(Date, nullable=True)
    AreaID = Column(Integer, ForeignKey("areas.AreaID"))
    CantidadTVBox = Column(Integer, nullable=True)
    CantidadRepetidor = Column(Integer, nullable=True)
    EstadoID = Column(Integer, ForeignKey("estadoscliente.EstadoID"))
    FechaCreacion = Column(TIMESTAMP, nullable=False)
    FechaActualizacion = Column(TIMESTAMP, nullable=False)
    Evaluacion = Column(String(10), nullable=True)
    UsuarioID = Column(Integer, ForeignKey("usuarios.UsuarioID"))
    cajaID = Column(Integer, ForeignKey("cajas.cajaID"))
    CondominioID = Column(Integer, ForeignKey("condominios.CondominioID"))
    tipo_cliente = Column(Enum("Nuevo", "Existente", name="tipo_cliente_enum"), default="Nuevo")

    # Relaciones con departamento
    departamento = relationship("Departamento", back_populates="clientes")
    
    # Relaciones con provincia
    provincia = relationship("Provincia", back_populates="clientes")
    
    # Relaciones con distrito
    distrito = relationship("Distrito", back_populates="clientes")
    
    # Relaciones con tipo de servicio
    tiposervicio = relationship("TipoServicio", back_populates="clientes")
    
    # Relaciones con plan
    plan = relationship("Plan", back_populates="clientes")
    
    # Relaciones con promocion
    promocion = relationship("Promocion", back_populates="clientes")
    
    # Relaciones con area
    area = relationship("Area", back_populates="clientes")
    
    # Relaciones con estado
    estado = relationship("EstadoCliente", back_populates="clientes")
    
    # Relaciones con caja
    caja = relationship("Caja", back_populates="clientes")
    
    # Relaciones con condominio
    condominio = relationship("Condominio", back_populates="clientes")

    # Relación con ClienteUsuario
    usuarios = relationship("ClienteUsuario", back_populates="cliente")

    # Relación con comentariosclientes
    comentarios = relationship("ComentarioCliente", back_populates="cliente")

    def to_dict(self):
        return {
            "ClienteID": self.ClienteID,
            "NumeroIdentificacion": self.NumeroIdentificacion,
            "TipoDocumento": self.TipoDocumento,
            "NombreCompleto": self.NombreCompleto,
            "Direccion": self.Direccion,
            "DepartamentoID": self.DepartamentoID,
            "ProvinciaID": self.ProvinciaID,
            "DistritoID": self.DistritoID,
            "CoordenadasGPS": self.CoordenadasGPS,
            "Telefono": self.Telefono,
            "Correo": self.Correo,
            "RecomendadoPor": self.RecomendadoPor,
            "NombreRecomendado": self.NombreRecomendado,
            "TipoServicioID": self.TipoServicioID,
            "PlanID": self.PlanID,
            "PromoID": self.PromoID,
            "Fecha": str(self.Fecha),
            "AreaID": self.AreaID,
            "CantidadTVBox": self.CantidadTVBox,
            "CantidadRepetidor": self.CantidadRepetidor,
            "EstadoID": self.EstadoID,
            "FechaCreacion": str(self.FechaCreacion),
            "FechaActualizacion": str(self.FechaActualizacion),
            "Evaluacion": self.Evaluacion,
            "UsuarioID": self.UsuarioID,
            "cajaID": self.cajaID,
            "CondominioID": self.CondominioID,
            "tipo_cliente": self.tipo_cliente,
        }
# Validador
    @validates("tipo_cliente")
    def validate_tipo_cliente(self, key, value):
        if value not in ["Nuevo", "Existente"]:
            raise ValueError(f"El valor '{value}' para 'tipo_cliente' no es válido. Debe ser 'Nuevo' o 'Existente'.")
        return value