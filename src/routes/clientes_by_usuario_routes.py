from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from database.db_mysql import get_db
from sqlalchemy.orm import Session
from services.clientes_by_usuario_service import get_clientes_by_usuario

clientes_by_usuario_bp = Blueprint("clientes_by_usuario", __name__)

@clientes_by_usuario_bp.route("/clientes/por-usuario", methods=["GET"])
@jwt_required()
def filter_clientes_by_usuario():
    db: Session = next(get_db())

    try:
        # Obtener el UsuarioID desde los parámetros de la solicitud
        usuario_id = request.args.get("usuario_id", type=int)
        if not usuario_id:
            return jsonify({"error": "El parámetro 'usuario_id' es obligatorio."}), 400

        # Llamar al servicio para obtener los clientes por usuario
        clientes = get_clientes_by_usuario(db, usuario_id)

        if not clientes:
            return jsonify({"message": "No se encontraron clientes para el UsuarioID proporcionado."}), 404

        return jsonify({"clientes": clientes}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Ocurrió un error inesperado.", "details": str(e)}), 500
