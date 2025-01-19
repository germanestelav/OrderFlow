from sqlalchemy.orm import Session
from models.cliente import Cliente
from datetime import datetime

# Crear un nuevo cliente
def create_cliente(
    db, data,
    NumeroIdentificacion,
    TipoDocumento,
    NombreCompleto,
    Direccion,
    DepartamentoID,
    ProvinciaID,
    DistritoID,
    CoordenadasGPS,
    Telefono,
    Correo,
    RecomendadoPor,
    NombreRecomendado,
    TipoServicioID,
    PlanID,
    PromoID,
    Fecha,
    AreaID,
    CantidadTVBox,
    CantidadRepetidor,
    EstadoID,
    Evaluacion,
    UsuarioID,
    cajaID,
    CondominioID,
    tipo_cliente
):
    # Validar el valor de 'tipo_cliente'
    tipo_cliente = data.get("tipo_cliente", "Nuevo")
    if tipo_cliente not in ["Nuevo", "Existente"]:
        raise ValueError(f"El valor '{tipo_cliente}' no es válido para 'tipo_cliente'. Solo se permiten 'Nuevo' o 'Existente'.")

    nuevo_cliente = Cliente(
        NumeroIdentificacion=NumeroIdentificacion,
        TipoDocumento=TipoDocumento,
        NombreCompleto=NombreCompleto,
        Direccion=Direccion,
        DepartamentoID=DepartamentoID,
        ProvinciaID=ProvinciaID,
        DistritoID=DistritoID,
        CoordenadasGPS=CoordenadasGPS,
        Telefono=Telefono,
        Correo=Correo,
        RecomendadoPor=RecomendadoPor,
        NombreRecomendado=NombreRecomendado,
        TipoServicioID=TipoServicioID,
        PlanID=PlanID,
        PromoID=PromoID,
        Fecha=Fecha,
        AreaID=AreaID,
        CantidadTVBox=CantidadTVBox,
        CantidadRepetidor=CantidadRepetidor,
        EstadoID=EstadoID,
        Evaluacion=Evaluacion,
        UsuarioID=UsuarioID,
        cajaID=cajaID,
        CondominioID=CondominioID,
        tipo_cliente=tipo_cliente
    )
    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)
    return nuevo_cliente

# Obtener todos los clientes
def get_clientes(db):
    return db.query(Cliente).all()

# Obtener un cliente por ID
def get_cliente_by_id(db, cliente_id):
    return db.query(Cliente).filter(Cliente.ClienteID == cliente_id).first()

# Actualizar un cliente
def update_cliente(db, cliente_id, data):
    # Buscar el cliente existente
    cliente = db.query(Cliente).filter(Cliente.ClienteID == cliente_id).first()
    if not cliente:
        return None

    # Validar el campo 'tipo_cliente'
    tipo_cliente = data.get("tipo_cliente", cliente.tipo_cliente)
    if tipo_cliente not in ["Nuevo", "Existente"]:
        raise ValueError(f"El valor '{tipo_cliente}' no es válido para 'tipo_cliente'. Solo se permiten 'Nuevo' o 'Existente'.")

    # Actualizar los campos del cliente
    cliente.NumeroIdentificacion = data.get("NumeroIdentificacion", cliente.NumeroIdentificacion)
    cliente.TipoDocumento = data.get("TipoDocumento", cliente.TipoDocumento)
    cliente.NombreCompleto = data.get("NombreCompleto", cliente.NombreCompleto)
    cliente.Direccion = data.get("Direccion", cliente.Direccion)
    cliente.DepartamentoID = data.get("DepartamentoID", cliente.DepartamentoID)
    cliente.ProvinciaID = data.get("ProvinciaID", cliente.ProvinciaID)
    cliente.DistritoID = data.get("DistritoID", cliente.DistritoID)
    cliente.CoordenadasGPS = data.get("CoordenadasGPS", cliente.CoordenadasGPS)
    cliente.Telefono = data.get("Telefono", cliente.Telefono)
    cliente.Correo = data.get("Correo", cliente.Correo)
    cliente.RecomendadoPor = data.get("RecomendadoPor", cliente.RecomendadoPor)
    cliente.NombreRecomendado = data.get("NombreRecomendado", cliente.NombreRecomendado)
    cliente.TipoServicioID = data.get("TipoServicioID", cliente.TipoServicioID)
    cliente.PlanID = data.get("PlanID", cliente.PlanID)
    cliente.PromoID = data.get("PromoID", cliente.PromoID)
    cliente.Fecha = data.get("Fecha", cliente.Fecha)
    cliente.AreaID = data.get("AreaID", cliente.AreaID)
    cliente.CantidadTVBox = data.get("CantidadTVBox", cliente.CantidadTVBox)
    cliente.CantidadRepetidor = data.get("CantidadRepetidor", cliente.CantidadRepetidor)
    cliente.EstadoID = data.get("EstadoID", cliente.EstadoID)
    cliente.Evaluacion = data.get("Evaluacion", cliente.Evaluacion)
    cliente.UsuarioID = data.get("UsuarioID", cliente.UsuarioID)
    cliente.cajaID = data.get("cajaID", cliente.cajaID)
    cliente.CondominioID = data.get("CondominioID", cliente.CondominioID)
    cliente.tipo_cliente = tipo_cliente

    # Actualizamos la fecha de actualización
    cliente.FechaActualizacion = datetime.utcnow()

    # Guardar los cambios en la base de datos
    db.commit()
    db.refresh(cliente)
    return cliente

# Eliminar un cliente
def delete_cliente(db, cliente_id):
    cliente = get_cliente_by_id(db, cliente_id)
    if not cliente:
        return None

    db.delete(cliente)
    db.commit()
    return cliente