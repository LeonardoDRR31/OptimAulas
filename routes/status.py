# routes/status.py
from flask import Blueprint, jsonify

status_bp = Blueprint('status_bp', __name__)

@status_bp.route('/status', methods=['GET'])
def status():
    return jsonify({"message": "Backend funcionando"})
