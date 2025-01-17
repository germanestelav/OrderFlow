from models.rol import Rol

# Crear una nuevo rol
def create_rol(db, nombre_rol):
    nuevo_rol = Rol(NombreRol=nombre_rol)
    db.add(nuevo_rol)
    db.commit()
    db.refresh(nuevo_rol)
    return nuevo_rol

# Obtener todos los roles
def get_roles(db):
    return db.query(Rol).all()

# Obtener los roles por ID
def get_rol_by_id(db, rol_id):
    return db.query(Rol).filter(Rol.RolID == rol_id).first()

# Actualizar un rol
def update_rol(db, rol_id, nombre_rol):
    rol = get_rol_by_id(db, rol_id)
    if not rol:
        return None

    rol.NombreRol = nombre_rol
    db.commit()
    db.refresh(rol)
    return rol

# Eliminar un rol
def delete_rol(db, rol_id):
    rol = get_rol_by_id(db, rol_id)
    if not rol:
        return None

    db.delete(rol)
    db.commit()
    return rol
