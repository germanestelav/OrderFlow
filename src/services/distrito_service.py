from models.distrito import Distrito

# Crear un nuevo distrito
def create_distrito(db, nombre, provincia_id):
    nuevo_distrito = Distrito(Nombre=nombre, ProvinciaID=provincia_id)
    db.add(nuevo_distrito)
    db.commit()
    db.refresh(nuevo_distrito)
    return nuevo_distrito

# Obtener todos los distritos
def get_distritos(db):
    return db.query(Distrito).all()

# Obtener distrito por ID
def get_distrito_by_id(db, distrito_id):
    return db.query(Distrito).filter(Distrito.DistritoID == distrito_id).first()

# Actualizar un distrito
def update_distrito(db, distrito_id, nombre, provincia_id):
    distrito = get_distrito_by_id(db, distrito_id)
    if not distrito:
        return None

    distrito.Nombre = nombre
    distrito.ProvinciaID = provincia_id
    db.commit()
    db.refresh(distrito)
    return distrito

# Eliminar un distrito
def delete_distrito(db, distrito_id):
    distrito = get_distrito_by_id(db, distrito_id)
    if not distrito:
        return None

    db.delete(distrito)
    db.commit()
    return distrito
