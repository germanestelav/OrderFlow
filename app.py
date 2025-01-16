import sys
import os

# Agrega el directorio 'src' al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from flask import Flask
from routes.area_routes import area_bp
from routes.caja_routes import caja_bp

app = Flask(__name__)

# Registrar las rutas de áreas

app.register_blueprint(area_bp, url_prefix="/api")
app.register_blueprint(caja_bp, url_prefix="/api")

@app.route("/")
def root():
    return {"message": "API de Áreas Activa"}


if __name__ == "__main__":
    app.run(debug=True)
