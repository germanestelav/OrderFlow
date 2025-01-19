from models.cliente_usuario import ClienteUsuario
from models.usuario import Usuario
from models.cliente import Cliente
from models.cliente_usuario import ClienteUsuario

# Crear un cliente_usuario
def create_cliente_usuario(db, UsuarioID, ClienteID):
    nuevo_cliente_usuario = ClienteUsuario(UsuarioID=UsuarioID, ClienteID=ClienteID)
    db.add(nuevo_cliente_usuario)
    db.commit()
    db.refresh(nuevo_cliente_usuario)
    return nuevo_cliente_usuario

# Obtener los clientes_usuarios
def get_cliente_usuarios(db):
    return db.query(ClienteUsuario).all()

# Obtener un cliente_usuario por ID
def get_cliente_usuario_by_id(db, id):
    return db.query(ClienteUsuario).filter(ClienteUsuario.id == id).first()

# Actualizar un cliente_usuario
def update_cliente_usuario(db, cliente_usuario_id, data):
    # Validar que el UsuarioID existe
    usuario = db.query(Usuario).filter(Usuario.UsuarioID == data["UsuarioID"]).first()
    if not usuario:
        raise ValueError(f"UsuarioID {data['UsuarioID']} no existe.")

    # Validar que el ClienteID existe (si se está actualizando también)
    cliente = db.query(Cliente).filter(Cliente.ClienteID == data["ClienteID"]).first()
    if not cliente:
        raise ValueError(f"ClienteID {data['ClienteID']} no existe.")

    # Continuar con la actualización
    cliente_usuario = db.query(ClienteUsuario).filter(ClienteUsuario.id == cliente_usuario_id).first()
    if not cliente_usuario:
        return None

    cliente_usuario.UsuarioID = data.get("UsuarioID", cliente_usuario.UsuarioID)
    cliente_usuario.ClienteID = data.get("ClienteID", cliente_usuario.ClienteID)

    db.commit()
    db.refresh(cliente_usuario)
    return cliente_usuario

# Eliminar un cliente_usuario
def delete_cliente_usuario(db, id):
    cliente_usuario = get_cliente_usuario_by_id(db, id)
    if not cliente_usuario:
        return None
    db.delete(cliente_usuario)
    db.commit()
    return cliente_usuario
