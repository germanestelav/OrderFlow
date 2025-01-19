from flask import Blueprint, request, jsonify
from database.db_mysql import get_db
from sqlalchemy.orm import Session
from models.cliente import Cliente
from services.cliente_service import (
    get_clientes,
    get_cliente_by_id,
    create_cliente,
    update_cliente,
    delete_cliente
)

cliente_bp = Blueprint("clientes", __name__)

@cliente_bp.route("/clientes", methods=["GET"])
def get_clientes_endpoint():
    db = next(get_db())
    clientes = get_clientes(db)
    return jsonify([cliente.to_dict() for cliente in clientes])

@cliente_bp.route("/clientes/<int:cliente_id>", methods=["GET"])
def get_cliente_by_id_endpoint(cliente_id):
    db = next(get_db())
    cliente = get_cliente_by_id(db, cliente_id)
    if not cliente:
        return jsonify({"error": "Cliente no encontrado"}), 404
    return jsonify(cliente.to_dict())

@cliente_bp.route("/clientes", methods=["POST"])
def create_cliente_endpoint():
    db: Session = next(get_db())
    data = request.json
    try:
        # Llamamos a la función del servicio con los datos del cliente
        nuevo_cliente = create_cliente(db, data)
        return jsonify(nuevo_cliente.to_dict()), 201
    except ValueError as e:
        # Capturamos errores de validación y devolvemos un mensaje claro
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Capturamos errores genéricos y devolvemos un mensaje general
        return jsonify({"error": "Ocurrió un error inesperado. Por favor, inténtalo de nuevo."}), 500  

def create_cliente(db, data):
    # Validar el campo 'tipo_cliente'
    tipo_cliente = data.get("tipo_cliente", "Nuevo")
    if tipo_cliente not in ["Nuevo", "Existente"]:
        raise ValueError(f"El valor '{tipo_cliente}' no es válido para 'tipo_cliente'. Solo se permiten 'Nuevo' o 'Existente'.")

    # Crear el cliente
    nuevo_cliente = Cliente(
        NumeroIdentificacion=data.get("NumeroIdentificacion"),
        TipoDocumento=data.get("TipoDocumento"),
        NombreCompleto=data.get("NombreCompleto"),
        Direccion=data.get("Direccion"),
        DepartamentoID=data.get("DepartamentoID"),
        ProvinciaID=data.get("ProvinciaID"),
        DistritoID=data.get("DistritoID"),
        CoordenadasGPS=data.get("CoordenadasGPS"),
        Telefono=data.get("Telefono"),
        Correo=data.get("Correo"),
        RecomendadoPor=data.get("RecomendadoPor"),
        NombreRecomendado=data.get("NombreRecomendado"),
        TipoServicioID=data.get("TipoServicioID"),
        PlanID=data.get("PlanID"),
        PromoID=data.get("PromoID"),
        Fecha=data.get("Fecha"),
        AreaID=data.get("AreaID"),
        CantidadTVBox=data.get("CantidadTVBox"),
        CantidadRepetidor=data.get("CantidadRepetidor"),
        EstadoID=data.get("EstadoID"),
        Evaluacion=data.get("Evaluacion"),
        UsuarioID=data.get("UsuarioID"),
        cajaID=data.get("cajaID"),
        CondominioID=data.get("CondominioID"),
        tipo_cliente=tipo_cliente
    )
    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)
    return nuevo_cliente


@cliente_bp.route("/clientes/<int:cliente_id>", methods=["PUT"])
def update_cliente_endpoint(cliente_id):
    db: Session = next(get_db())
    data = request.json

    try:
        cliente_actualizado = update_cliente(db, cliente_id, data)
        if not cliente_actualizado:
            return jsonify({"error": "Cliente no encontrado"}), 404
        return jsonify(cliente_actualizado.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Ocurrió un error inesperado.", "details": str(e)}), 500

@cliente_bp.route("/clientes/<int:cliente_id>", methods=["DELETE"])
def delete_cliente_endpoint(cliente_id):
    db: Session = next(get_db())
    cliente_eliminado = delete_cliente(db, cliente_id)
    if not cliente_eliminado:
        return jsonify({"error": "Cliente no encontrado"}), 404
    return jsonify({"message": "Cliente eliminado con éxito"})
