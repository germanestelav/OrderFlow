from sqlalchemy.orm import Session
from models.comentariosclientes import ComentarioCliente
from models.cliente import Cliente
from models.usuario import Usuario
from sqlalchemy.exc import IntegrityError

#Crear comentario_cliente
def create_comentario_cliente(db: Session, data: dict):
    cliente = db.query(Cliente).filter(Cliente.ClienteID == data["ClienteID"]).first()
    if not cliente:
        raise ValueError(f"ClienteID {data['ClienteID']} no existe.")
    
    usuario = db.query(Usuario).filter(Usuario.UsuarioID == data["UsuarioID"]).first()
    if not usuario:
        raise ValueError(f"UsuarioID {data['UsuarioID']} no existe.")
    
    comentario = ComentarioCliente(
        ClienteID=data["ClienteID"],
        UsuarioID=data["UsuarioID"],
        Comentario=data["Comentario"]
    )
    db.add(comentario)
    try:
        db.commit()
        db.refresh(comentario)
    except IntegrityError as e:
        db.rollback()
        raise ValueError(f"Error de integridad: {str(e)}")
    return comentario

#Obtener todos los comentario_cliente
def get_comentarios_clientes(db: Session):
    return db.query(ComentarioCliente).all()

#Obtener comentario_cliente por ID
def get_comentario_cliente_by_id(db: Session, comentario_id: int):
    return db.query(ComentarioCliente).filter(ComentarioCliente.ComentarioID == comentario_id).first()

#Actualizar comentario_cliente
def update_comentario_cliente(db, comentario_id, data):
    comentario = db.query(ComentarioCliente).filter(ComentarioCliente.ComentarioID == comentario_id).first()
    if not comentario:
        return None
    
    # Actualiza solo los campos enviados en el request
    comentario.ClienteID = data.get("ClienteID", comentario.ClienteID)
    comentario.UsuarioID = data.get("UsuarioID", comentario.UsuarioID)
    comentario.Comentario = data.get("Comentario", comentario.Comentario)
    
    # FechaHora se actualizará automáticamente gracias a onupdate=func.now()
    db.commit()
    db.refresh(comentario)
    return comentario

#Eliminar comentario_cliente
def delete_comentario_cliente(db: Session, comentario_id: int):
    comentario = db.query(ComentarioCliente).filter(ComentarioCliente.ComentarioID == comentario_id).first()
    if not comentario:
        return None
    db.delete(comentario)
    db.commit()
    return comentario
