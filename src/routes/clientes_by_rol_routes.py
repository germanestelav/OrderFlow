from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from database.db_mysql import get_db
from sqlalchemy.orm import Session
from services.clientes_by_rol_service import get_clientes_by_rol

clientes_by_rol_bp = Blueprint("clientes_by_rol", __name__)

@clientes_by_rol_bp.route("/clientes/por-rol", methods=["GET"])
@jwt_required()
def filter_clientes_by_rol():
    db: Session = next(get_db())

    try:
        # Obtener el RolID desde los parámetros de la solicitud
        rol_id = request.args.get("rol_id", type=int)
        if not rol_id:
            return jsonify({"error": "El parámetro 'rol_id' es obligatorio."}), 400

        # Llamar al servicio para obtener los clientes por rol
        clientes = get_clientes_by_rol(db, rol_id)

        if not clientes:
            return jsonify({"message": "No se encontraron clientes para el RolID proporcionado."}), 404

        return jsonify({"clientes": clientes}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Ocurrió un error inesperado.", "details": str(e)}), 500
