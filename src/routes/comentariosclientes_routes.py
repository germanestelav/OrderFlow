from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from sqlalchemy.orm import Session
from database.db_mysql import get_db
from services.comentariosclientes_service import (
    create_comentario_cliente,
    get_comentarios_clientes,
    get_comentario_cliente_by_id,
    update_comentario_cliente,
    delete_comentario_cliente
)

comentarios_clientes_bp = Blueprint("comentarios_clientes", __name__)

@comentarios_clientes_bp.route("/comentariosclientes", methods=["POST"])
@jwt_required()
def create_comentario_cliente_endpoint():
    db: Session = next(get_db())
    data = request.json
    try:
        nuevo_comentario = create_comentario_cliente(db, data)
        return jsonify(nuevo_comentario.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Ocurrió un error inesperado.", "details": str(e)}), 500

@comentarios_clientes_bp.route("/comentariosclientes", methods=["GET"])
@jwt_required()
def get_comentarios_clientes_endpoint():
    db: Session = next(get_db())
    comentarios = get_comentarios_clientes(db)
    return jsonify([comentario.to_dict() for comentario in comentarios])

@comentarios_clientes_bp.route("/comentariosclientes/<int:comentario_id>", methods=["GET"])
@jwt_required()
def get_comentario_cliente_by_id_endpoint(comentario_id):
    db: Session = next(get_db())
    comentario = get_comentario_cliente_by_id(db, comentario_id)
    if not comentario:
        return jsonify({"error": "Comentario no encontrado"}), 404
    return jsonify(comentario.to_dict())

@comentarios_clientes_bp.route("/comentariosclientes/<int:comentario_id>", methods=["PUT"])
@jwt_required()
def update_comentario_cliente_endpoint(comentario_id):
    db: Session = next(get_db())
    data = request.json
    try:
        comentario_actualizado = update_comentario_cliente(db, comentario_id, data)
        if not comentario_actualizado:
            return jsonify({"error": "Comentario no encontrado"}), 404
        return jsonify(comentario_actualizado.to_dict())
    except Exception as e:
        return jsonify({"error": "Ocurrió un error inesperado.", "details": str(e)}), 500

@comentarios_clientes_bp.route("/comentariosclientes/<int:comentario_id>", methods=["DELETE"])
@jwt_required()
def delete_comentario_cliente_endpoint(comentario_id):
    db: Session = next(get_db())
    try:
        comentario_eliminado = delete_comentario_cliente(db, comentario_id)
        if not comentario_eliminado:
            return jsonify({"error": "Comentario no encontrado"}), 404
        return jsonify({"message": "Comentario eliminado con éxito"}), 200
    except Exception as e:
        return jsonify({"error": "Ocurrió un error inesperado.", "details": str(e)}), 500
