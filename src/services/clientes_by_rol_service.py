from sqlalchemy.orm import Session
from models.cliente import Cliente
from models.usuario import Usuario
from models.rol import Rol
from models.usuario_rol import UsuarioRol
from models.cliente_usuario import ClienteUsuario

def get_clientes_by_rol(db: Session, rol_id: int):
    try:
        # Consulta para obtener clientes asociados al RolID especificado
        clientes = (
            db.query(Cliente)
            .join(ClienteUsuario, Cliente.ClienteID == ClienteUsuario.ClienteID)
            .join(Usuario, Usuario.UsuarioID == ClienteUsuario.UsuarioID)
            .join(UsuarioRol, Usuario.UsuarioID == UsuarioRol.UsuarioID)
            .join(Rol, Rol.RolID == UsuarioRol.RolID)
            .filter(Rol.RolID == rol_id)
            .all()
        )

        # Retornar los clientes en formato de lista de diccionarios
        return [cliente.to_dict() for cliente in clientes]

    except Exception as e:
        raise ValueError(f"Error al obtener clientes por rol: {str(e)}")
