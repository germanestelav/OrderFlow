from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.db_mysql import get_db
from models.comentariosclientes import ComentarioCliente
from services.comments_service import update_comment_service

comments_bp = Blueprint("comments", __name__)

@comments_bp.route("/comentarios/<int:comentario_id>", methods=["PUT"])
@jwt_required()
def update_comment(comentario_id):
    db = next(get_db())
    data = request.json

    try:
        # Obtener el ID del usuario autenticado desde el token JWT
        usuario_id = get_jwt_identity()

        # Buscar el comentario en la base de datos
        comentario = db.query(ComentarioCliente).filter_by(ComentarioID=comentario_id).first()

        if not comentario:
            return jsonify({"error": "El comentario no existe."}), 404

        # Validar que el usuario autenticado sea el creador del comentario
        if int(comentario.UsuarioID) != int(usuario_id):
            return jsonify({
                "error": "No tienes permisos para editar este comentario.",
                "detalles": {
                    "UsuarioAutenticado": usuario_id,
                    "UsuarioCreador": comentario.UsuarioID
                }
            }), 403

        # Actualizar el comentario si el usuario tiene permiso
        comentario.Comentario = data.get("Comentario", comentario.Comentario)
        comentario.FechaHora = data.get("FechaHora", comentario.FechaHora)
        db.commit()

        return jsonify({"message": "Comentario actualizado correctamente."}), 200

    except Exception as e:
        return jsonify({"error": "Ocurrió un error inesperado.", "details": str(e)}), 500
