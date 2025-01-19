import sys
import os

# Agrega el directorio 'src' al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from flask import Flask
from routes.area_routes import area_bp
from routes.caja_routes import caja_bp
from routes.departamento_routes import departamento_bp
from routes.estado_cliente_routes import estado_cliente_bp
from routes.plan_routes import plan_bp
from routes.promocion_routes import promocion_bp
from routes.rol_routes import rol_bp
from routes.tipo_servicio_routes import tipo_servicio_bp
from routes.provincia_routes import provincia_bp
from routes.distrito_routes import distrito_bp
from routes.condominio_routes import condominio_bp
from routes.usuario_routes import usuario_bp
from routes.usuario_rol_routes import usuario_rol_bp
from routes.cliente_routes import cliente_bp
from routes.cliente_usuario_routes import cliente_usuario_bp
from routes.comentariosclientes_routes import comentarios_clientes_bp

app = Flask(__name__)

# Registrar las rutas de áreas
app.register_blueprint(area_bp, url_prefix="/api")
app.register_blueprint(caja_bp, url_prefix="/api")
app.register_blueprint(departamento_bp, url_prefix="/api")
app.register_blueprint(estado_cliente_bp, url_prefix="/api")
app.register_blueprint(plan_bp, url_prefix="/api")
app.register_blueprint(promocion_bp, url_prefix="/api")
app.register_blueprint(rol_bp, url_prefix="/api")
app.register_blueprint(tipo_servicio_bp, url_prefix="/api")
app.register_blueprint(provincia_bp, url_prefix="/api")
app.register_blueprint(distrito_bp, url_prefix="/api")
app.register_blueprint(condominio_bp, url_prefix="/api")
app.register_blueprint(usuario_bp, url_prefix="/api")
app.register_blueprint(usuario_rol_bp, url_prefix="/api")
app.register_blueprint(cliente_bp, url_prefix="/api")
app.register_blueprint(cliente_usuario_bp, url_prefix="/api")
app.register_blueprint(comentarios_clientes_bp, url_prefix="/api")

@app.route("/")
def root():
    return {"message": "API de Áreas Activa"}


if __name__ == "__main__":
    app.run(debug=True)
