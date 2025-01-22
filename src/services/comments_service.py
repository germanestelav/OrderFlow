from sqlalchemy.orm import Session
from models.comentariosclientes import ComentarioCliente

def update_comment_service(db: Session, comentario_id: int, usuario_id: int, data: dict):
    # Buscar el comentario en la base de datos
    comentario = db.query(ComentarioCliente).filter_by(ComentarioID=comentario_id).first()

    if not comentario:
        raise ValueError("El comentario no existe.")

    # Validar que el usuario autenticado sea el creador del comentario
    if comentario.UsuarioID != usuario_id:
        raise PermissionError("No tienes permisos para editar este comentario.")
        

    # Actualizar el comentario
    comentario.Comentario = data.get("Comentario", comentario.Comentario)
    comentario.FechaHora = data.get("FechaHora", comentario.FechaHora)
    db.commit()

    return comentario
