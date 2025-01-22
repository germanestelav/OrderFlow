from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from sqlalchemy.orm import Session
from database.db_mysql import get_db
from services.usuario_service import (
    get_usuarios, get_usuario_by_id, create_usuario, update_usuario, delete_usuario
)

usuario_bp = Blueprint("usuarios", __name__)

@usuario_bp.route("/usuarios", methods=["GET"])
@jwt_required()
def get_usuarios_endpoint():
    db: Session = next(get_db())
    usuarios = get_usuarios(db)
    return jsonify([usuario.to_dict() for usuario in usuarios])

@usuario_bp.route("/usuarios/<int:usuario_id>", methods=["GET"])
@jwt_required()
def get_usuario_by_id_endpoint(usuario_id):
    db: Session = next(get_db())
    usuario = get_usuario_by_id(db, usuario_id)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(usuario.to_dict())

@usuario_bp.route("/usuarios", methods=["POST"])
@jwt_required()
def create_usuario_endpoint():
    db: Session = next(get_db())
    data = request.json
    nuevo_usuario = create_usuario(db, data)
    return jsonify(nuevo_usuario.to_dict()), 201

@usuario_bp.route("/usuarios/<int:usuario_id>", methods=["PUT"])
@jwt_required()
def update_usuario_endpoint(usuario_id):
    db: Session = next(get_db())
    data = request.json
    usuario_actualizado = update_usuario(db, usuario_id, data)
    if not usuario_actualizado:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(usuario_actualizado.to_dict())

@usuario_bp.route("/usuarios/<int:usuario_id>", methods=["DELETE"])
@jwt_required()
def delete_usuario_endpoint(usuario_id):
    db: Session = next(get_db())
    usuario_eliminado = delete_usuario(db, usuario_id)
    if not usuario_eliminado:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify({"message": "Usuario eliminado con éxito"})
