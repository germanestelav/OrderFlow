from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from sqlalchemy.orm import Session
from database.db_mysql import get_db
from services.usuario_rol_service import (
    get_usuariosroles, get_usuariorol_by_id, create_usuariorol, update_usuariorol, delete_usuariorol
)

usuario_rol_bp = Blueprint("usuariosroles", __name__)

@usuario_rol_bp.route("/usuariosroles", methods=["GET"])
@jwt_required()
def get_usuariosroles_endpoint():
    db: Session = next(get_db())
    usuariosroles = get_usuariosroles(db)
    return jsonify([usuariorol.to_dict() for usuariorol in usuariosroles])

@usuario_rol_bp.route("/usuariosroles/<int:usuariosroles_id>", methods=["GET"])
@jwt_required()
def get_usuariorol_by_id_endpoint(usuariosroles_id):
    db: Session = next(get_db())
    usuariorol = get_usuariorol_by_id(db, usuariosroles_id)
    if not usuariorol:
        return jsonify({"error": "UsuarioRol no encontrado"}), 404
    return jsonify(usuariorol.to_dict())

@usuario_rol_bp.route("/usuariosroles", methods=["POST"])
@jwt_required()
def create_usuariorol_endpoint():
    db: Session = next(get_db())
    data = request.json

    try:
        nuevo_usuariorol = create_usuariorol(db, data)
        return jsonify(nuevo_usuariorol.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@usuario_rol_bp.route("/usuariosroles/<int:usuariosroles_id>", methods=["PUT"])
@jwt_required()
def update_usuariorol_endpoint(usuariosroles_id):
    db: Session = next(get_db())
    data = request.json

    try:
        usuariorol_actualizado = update_usuariorol(db, usuariosroles_id, data)
        return jsonify(usuariorol_actualizado.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@usuario_rol_bp.route("/usuariosroles/<int:usuariosroles_id>", methods=["DELETE"])
@jwt_required()
def delete_usuariorol_endpoint(usuariosroles_id):
    db: Session = next(get_db())
    usuariorol_eliminado = delete_usuariorol(db, usuariosroles_id)
    if not usuariorol_eliminado:
        return jsonify({"error": "UsuarioRol no encontrado"}), 404
    return jsonify({"message": "UsuarioRol eliminado con éxito"})
