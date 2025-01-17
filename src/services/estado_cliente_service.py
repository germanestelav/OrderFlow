from sqlalchemy.orm import Session
from models.estado_cliente import EstadoCliente

# Crear un estado
def create_estado_cliente(db: Session, nombre):
    nuevo_estado = EstadoCliente(Nombre=nombre)
    db.add(nuevo_estado)
    db.commit()
    db.refresh(nuevo_estado)
    return nuevo_estado

# Obtener todos los estados
def get_estados_cliente(db: Session):
    return db.query(EstadoCliente).all()

# Obtener los estados por ID
def get_estado_cliente_by_id(db: Session, estado_id):
    return db.query(EstadoCliente).filter(EstadoCliente.EstadoID == estado_id).first()

# Eliminar un estado
def update_estado_cliente(db: Session, estado_id, nombre):
    estado = db.query(EstadoCliente).filter(EstadoCliente.EstadoID == estado_id).first()
    if estado:
        estado.Nombre = nombre
        db.commit()
        db.refresh(estado)
    return estado

def delete_estado_cliente(db: Session, estado_id):
    estado = db.query(EstadoCliente).filter(EstadoCliente.EstadoID == estado_id).first()
    if estado:
        db.delete(estado)
        db.commit()
    return estado
