
from flask import Flask, request, jsonify, send_file, render_template
from flask_cors import CORS
import pandas as pd
import numpy as np
import random
import json
import io
import os
from datetime import datetime, timedelta
import uuid

# Importar los Blueprints desacoplados
from routes.status import status_bp
from routes.upload import upload_bp
from routes.optimize import optimize_bp
from routes.download import download_bp

# Crear instancia de la app Flask
app = Flask(__name__)
CORS(app)  # Permitir solicitudes CORS (útil para desarrollo con frontend separado)

# Registrar blueprints
app.register_blueprint(status_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(optimize_bp)
app.register_blueprint(download_bp)

# Punto de entrada principal
if __name__ == '__main__':
    print("🚀 Iniciando OptimAulas UNS - Servidor Local")
    print("📍 URL: http://localhost:5000")
    print("📊 Endpoint de prueba: http://localhost:5000/status")
    print("⏹️  Para detener: Ctrl+C")
    app.run(debug=True, host='localhost', port=5000)