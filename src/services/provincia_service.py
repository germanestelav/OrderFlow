from models.provincia import Provincia

# Crear una nueva provincia
def create_provincia(db, nombre, departamento_id):
    nueva_provincia = Provincia(Nombre=nombre, DepartamentoID=departamento_id)
    db.add(nueva_provincia)
    db.commit()
    db.refresh(nueva_provincia)
    return nueva_provincia

# Obtener todos las provincias
def get_provincias(db):
    return db.query(Provincia).all()

# Obtener provincias por ID
def get_provincia_by_id(db, provincia_id):
    return db.query(Provincia).filter(Provincia.ProvinciaID == provincia_id).first()

# Actualizar una provincia
def update_provincia(db, provincia_id, nombre, departamento_id):
    provincia = get_provincia_by_id(db, provincia_id)
    if not provincia:
        return None

    provincia.Nombre = nombre
    provincia.DepartamentoID = departamento_id
    db.commit()
    db.refresh(provincia)
    return provincia

# Eliminar una provincia
def delete_provincia(db, provincia_id):
    provincia = get_provincia_by_id(db, provincia_id)
    if not provincia:
        return None

    db.delete(provincia)
    db.commit()
    return provincia
