from sqlalchemy.orm import Session
from models.usuario_rol import UsuarioRol
from sqlalchemy.exc import IntegrityError

# Obtener todos los usarios_roles
def get_usuariosroles(db: Session):
    return db.query(UsuarioRol).all()

# Obtener usuario_roles por ID
def get_usuariorol_by_id(db: Session, usuariosroles_id: int):
    return db.query(UsuarioRol).filter(UsuarioRol.usuariosroles_id == usuariosroles_id).first()

# Crear un nuevo usuario_rol
def create_usuariorol(db: Session, usuariorol_data: dict):
    try:
        # Crear el nuevo registro
        nuevo_usuariorol = UsuarioRol(**usuariorol_data)
        db.add(nuevo_usuariorol)
        db.commit()
        db.refresh(nuevo_usuariorol)
        return nuevo_usuariorol
    except IntegrityError as e:
        db.rollback()  # Deshacer cualquier cambio pendiente en la sesión
        raise ValueError("El usuario ya tiene asignado este rol.") from e

# Actualizar un usuario_rol
def update_usuariorol(db: Session, usuariosroles_id: int, usuariorol_data: dict):
    # Buscar el registro existente
    usuariorol = db.query(UsuarioRol).filter_by(usuariosroles_id=usuariosroles_id).first()

    if not usuariorol:
        raise ValueError("El registro no existe.")

    # Validar duplicados antes de actualizar
    existente = db.query(UsuarioRol).filter(
        UsuarioRol.UsuarioID == usuariorol_data.get("UsuarioID"),
        UsuarioRol.RolID == usuariorol_data.get("RolID"),
        UsuarioRol.usuariosroles_id != usuariosroles_id  # Excluir el registro actual
    ).first()

    if existente:
        raise ValueError(
            f"La combinación UsuarioID {usuariorol_data.get('UsuarioID')} y RolID {usuariorol_data.get('RolID')} ya existe."
        )

    # Actualizar el registro
    if "UsuarioID" in usuariorol_data:
        usuariorol.UsuarioID = usuariorol_data["UsuarioID"]
    if "RolID" in usuariorol_data:
        usuariorol.RolID = usuariorol_data["RolID"]
    if "estado" in usuariorol_data:
        usuariorol.estado = usuariorol_data["estado"]

    db.commit()
    db.refresh(usuariorol)
    return usuariorol

# Eliminar usuario_rol
def delete_usuariorol(db: Session, usuariosroles_id: int):
    usuariorol = get_usuariorol_by_id(db, usuariosroles_id)
    if not usuariorol:
        return None
    db.delete(usuariorol)
    db.commit()
    return usuariorol
