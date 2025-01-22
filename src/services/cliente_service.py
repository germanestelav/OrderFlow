from sqlalchemy.orm import Session
from models.cliente import Cliente
from datetime import datetime

# Crear un nuevo cliente
def create_cliente(db: Session, data: dict, usuario_id: int):
    print("Paso 1: Iniciando creación de cliente en el servicio")  # Depuración
    print(f"Datos recibidos: {data}")  # Depuración
    print(f"UsuarioID asociado: {usuario_id}")  # Depuración

    # Validar el valor de 'tipo_cliente'
    tipo_cliente = data.get("tipo_cliente", "Nuevo")
    print(f"Tipo de cliente: {tipo_cliente}")  # Depuración

    if tipo_cliente not in ["Nuevo", "Existente"]:
        print(f"Error: Tipo de cliente no válido - {tipo_cliente}")  # Depuración
        raise ValueError(f"El valor '{tipo_cliente}' no es válido para 'tipo_cliente'. Solo se permiten 'Nuevo' o 'Existente'.")

    # Crear el cliente con el UsuarioID asociado
    nuevo_cliente = Cliente(
        NumeroIdentificacion=data.get("NumeroIdentificacion"),
        TipoDocumento=data.get("TipoDocumento"),
        NombreCompleto=data.get("NombreCompleto"),
        Direccion=data.get("Direccion"),
        DepartamentoID=data.get("DepartamentoID"),
        ProvinciaID=data.get("ProvinciaID"),
        DistritoID=data.get("DistritoID"),
        CoordenadasGPS=data.get("CoordenadasGPS"),
        Telefono=data.get("Telefono"),
        Correo=data.get("Correo"),
        RecomendadoPor=data.get("RecomendadoPor"),
        NombreRecomendado=data.get("NombreRecomendado"),
        TipoServicioID=data.get("TipoServicioID"),
        PlanID=data.get("PlanID"),
        PromoID=data.get("PromoID"),
        Fecha=data.get("Fecha"),
        AreaID=data.get("AreaID"),
        CantidadTVBox=data.get("CantidadTVBox"),
        CantidadRepetidor=data.get("CantidadRepetidor"),
        EstadoID=data.get("EstadoID"),
        Evaluacion=data.get("Evaluacion"),
        UsuarioID=usuario_id,  # Asociar el UsuarioID
        cajaID=data.get("cajaID"),
        CondominioID=data.get("CondominioID"),
        tipo_cliente=tipo_cliente
    )

    print(f"Cliente creado: {nuevo_cliente}")  # Depuración
    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)
    print("Paso 2: Cliente guardado en la base de datos")  # Depuración
    return nuevo_cliente

# Obtener todos los clientes
def get_clientes(db):
    return db.query(Cliente).all()

# Obtener un cliente por ID
def get_cliente_by_id(db, cliente_id):
    return db.query(Cliente).filter(Cliente.ClienteID == cliente_id).first()

# Busca al cliente por nombre o número de identificación (DNI)
def get_cliente_by_name_or_id(db: Session, query: str):
    return db.query(Cliente).filter(
        (Cliente.NombreCompleto.like(f"%{query}%")) | (Cliente.NumeroIdentificacion == query)
    ).all()

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