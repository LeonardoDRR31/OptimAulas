# download.py
from flask import Blueprint, request, jsonify, send_file
import pandas as pd
import io
from datetime import datetime

download_bp = Blueprint('download', __name__)

@download_bp.route('/download_result', methods=['POST'])
def download_result():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se recibió un JSON válido"}), 400
        solution = data.get('solution', [])

        # Crear DataFrame
        df = pd.DataFrame(solution)

        # Crear archivo Excel en memoria
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Asignacion_Aulas', index=False)

        output.seek(0)

        return send_file(
            output,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name=f'asignacion_aulas_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'
        )

    except Exception as e:
        return jsonify({"error": f"Error generando descarga: {str(e)}"}), 500


@download_bp.route('/download_templates', methods=['GET'])
def download_templates():
    try:
        # Crear templates de ejemplo
        cursos_template = pd.DataFrame({
            'id': [1, 2, 3, 4, 5, 6],
            'nombre': ['Algoritmos I', 'Base de Datos', 'Lab Algoritmos I', 'Lab Base de Datos', 'Estructura de Datos', 'Redes'],
            'ciclo': [3, 4, 3, 4, 4, 6],
            'tipo': ['teoria', 'teoria', 'laboratorio', 'laboratorio', 'teoria', 'teoria'],
            'estudiantes': [40, 35, 15, 15, 42, 38],
            'duracion': [2, 2, 2, 2, 4, 2]
        })

        aulas_template = pd.DataFrame({
            'id': ['A101', 'A102', 'A103', 'LAB01', 'LAB02', 'EXT01', 'EXT02'],
            'nombre': ['Aula 101', 'Aula 102', 'Aula 103', 'Laboratorio 1', 'Laboratorio 2', 'Aula Externa 1', 'CECOMP Lab 1'],
            'tipo': ['teoria', 'teoria', 'teoria', 'laboratorio', 'laboratorio', 'externa', 'laboratorio'],
            'capacidad': [45, 45, 50, 15, 15, 50, 15],
            'ubicacion': ['Campus', 'Campus', 'Campus', 'Campus', 'Campus', 'Pool de Aulas', 'CECOMP'],
            'distancia': [0, 0, 0, 0, 0, 5, 8]
        })

        # Crear archivo Excel con múltiples hojas
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            cursos_template.to_excel(writer, sheet_name='Cursos', index=False)
            aulas_template.to_excel(writer, sheet_name='Aulas', index=False)

        output.seek(0)

        return send_file(
            output,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name='templates_asignacion_aulas.xlsx'
        )

    except Exception as e:
        return jsonify({"error": f"Error generando templates: {str(e)}"}), 500
