from flask import Blueprint, request, jsonify
import os
import uuid
from optimizer.aula_optimizer import AulaOptimizer

upload_bp = Blueprint('upload', __name__)
optimizer = AulaOptimizer()

@upload_bp.route('/upload', methods=['POST'])
def upload_files():
    try:
        if 'cursos' not in request.files or 'aulas' not in request.files:
            return jsonify({"error": "Faltan archivos requeridos"}), 400

        cursos_file = request.files['cursos']
        aulas_file = request.files['aulas']

        cursos_path = f"temp_cursos_{uuid.uuid4()}.xlsx"
        aulas_path = f"temp_aulas_{uuid.uuid4()}.xlsx"
        cursos_file.save(cursos_path)
        aulas_file.save(aulas_path)

        success, message = optimizer.load_data(cursos_path, aulas_path)

        os.remove(cursos_path)
        os.remove(aulas_path)

        if success:
            return jsonify({
                "success": True,
                "message": message,
                "stats": {
                    "cursos": len(optimizer.cursos),
                    "aulas": len(optimizer.aulas)
                }
            })
        else:
            return jsonify({"error": message}), 400

    except Exception as e:
        return jsonify({"error": f"Error procesando archivos: {str(e)}"}), 500
