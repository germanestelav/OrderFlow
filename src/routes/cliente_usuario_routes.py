from flask import Blueprint, request, jsonify
from database.db_mysql import get_db
from sqlalchemy.orm import Session
from models.usuario import Usuario
from models.cliente import Cliente
from services.cliente_usuario_service import (
    ClienteUsuario,
    get_cliente_usuarios,
    get_cliente_usuario_by_id,
    update_cliente_usuario,
    delete_cliente_usuario,
)

cliente_usuario_bp = Blueprint("cliente_usuario", __name__)

@cliente_usuario_bp.route("/clientesusuarios", methods=["POST"])
def create_cliente_usuario_endpoint():
    db: Session = next(get_db())
    data = request.json
    try:
        # Verificar que el UsuarioID existe
        usuario = db.query(Usuario).filter(Usuario.UsuarioID == data["UsuarioID"]).first()
        if not usuario:
            return jsonify({"error": f"UsuarioID {data['UsuarioID']} no existe"}), 400
        
        # Verificar que el ClienteID existe
        cliente = db.query(Cliente).filter(Cliente.ClienteID == data["ClienteID"]).first()
        if not cliente:
            return jsonify({"error": f"ClienteID {data['ClienteID']} no existe"}), 400
        
        # Crear la relación
        nuevo_cliente_usuario = ClienteUsuario(
            UsuarioID=data["UsuarioID"],
            ClienteID=data["ClienteID"]
        )
        db.add(nuevo_cliente_usuario)
        db.commit()
        db.refresh(nuevo_cliente_usuario)
        return jsonify(nuevo_cliente_usuario.to_dict()), 201
    except Exception as e:
        return jsonify({"error": "Ocurrió un error inesperado", "details": str(e)}), 500

@cliente_usuario_bp.route("/clientesusuarios", methods=["GET"])
def get_clientes_usuarios_endpoint():
    db: Session = next(get_db())
    try:
        clientes_usuarios = db.query(ClienteUsuario).all()
        return jsonify([cu.to_dict() for cu in clientes_usuarios]), 200
    except Exception as e:
        return jsonify({"error": "Ocurrió un error inesperado", "details": str(e)}), 500

@cliente_usuario_bp.route("/clientesusuarios/<int:id>", methods=["GET"])
def get_cliente_usuario_by_id_endpoint(id):
    db = next(get_db())
    cliente_usuario = get_cliente_usuario_by_id(db, id)
    if not cliente_usuario:
        return jsonify({"error": "ClienteUsuario no encontrado"}), 404
    return jsonify(cliente_usuario.to_dict())

@cliente_usuario_bp.route("/clientesusuarios/<int:cliente_usuario_id>", methods=["PUT"])
def update_cliente_usuario_endpoint(cliente_usuario_id):
    db: Session = next(get_db())
    data = request.json
    try:
        cliente_usuario_actualizado = update_cliente_usuario(db, cliente_usuario_id, data)
        if not cliente_usuario_actualizado:
            return jsonify({"error": "Registro no encontrado"}), 404
        return jsonify(cliente_usuario_actualizado.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Ocurrió un error inesperado", "details": str(e)}), 500


@cliente_usuario_bp.route("/clientesusuarios/<int:id>", methods=["DELETE"])
def delete_cliente_usuario_endpoint(id):
    db = next(get_db())
    cliente_usuario_eliminado = delete_cliente_usuario(db, id)
    if not cliente_usuario_eliminado:
        return jsonify({"error": "ClienteUsuario no encontrado"}), 404
    return jsonify({"message": "ClienteUsuario eliminado con éxito"})
