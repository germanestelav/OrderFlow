from werkzeug.security import check_password_hash
from models.usuario import Usuario

def verificar_credenciales(db, username, password):
    usuario = db.query(Usuario).filter(Usuario.NombreUsuario == username).first()
    print(f"Usuario encontrado: {usuario}")  # Mensaje de depuración
    if usuario and usuario.Contrasena == password:
        return usuario
    return None

