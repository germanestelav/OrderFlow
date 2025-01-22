from sqlalchemy.orm import Session
from models.cliente import Cliente
from models.cliente_usuario import ClienteUsuario

def get_clientes_by_usuario(db: Session, usuario_id: int):
    try:
        # Consulta para obtener los clientes asociados a un usuario
        clientes = (
            db.query(Cliente)
            .join(ClienteUsuario, Cliente.ClienteID == ClienteUsuario.ClienteID)
            .filter(ClienteUsuario.UsuarioID == usuario_id)
            .all()
        )

        # Retornar los clientes en formato de lista de diccionarios
        return [cliente.to_dict() for cliente in clientes]

    except Exception as e:
        raise ValueError(f"Error al obtener clientes por usuario: {str(e)}")
