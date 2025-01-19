from sqlalchemy.orm import Session
from models.usuario import Usuario

# Obtener todos los usuarios
def get_usuarios(db: Session):
    return db.query(Usuario).all()

# Obtener usuarios por ID
def get_usuario_by_id(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.UsuarioID == usuario_id).first()

# Crear un usuario
def create_usuario(db: Session, usuario_data: dict):
    nuevo_usuario = Usuario(**usuario_data)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

# Actualizar un usuario
def update_usuario(db: Session, usuario_id: int, usuario_data: dict):
    usuario = get_usuario_by_id(db, usuario_id)
    if not usuario:
        return None
    for key, value in usuario_data.items():
        setattr(usuario, key, value)
    db.commit()
    db.refresh(usuario)
    return usuario

# Eliminar un usuario
def delete_usuario(db: Session, usuario_id: int):
    usuario = get_usuario_by_id(db, usuario_id)
    if not usuario:
        return None
    db.delete(usuario)
    db.commit()
    return usuario
