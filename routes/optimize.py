from flask import Blueprint, jsonify
from optimizer.aula_optimizer import AulaOptimizer

optimize_bp = Blueprint('optimize', __name__)
optimizer = AulaOptimizer()

@optimize_bp.route('/optimize', methods=['POST'])
def optimize():
    try:
        if not optimizer.cursos or not optimizer.aulas:
            return jsonify({"error": "No hay datos cargados"}), 400

        best_solution, fitness_history = optimizer.genetic_algorithm()
        formatted_solution = optimizer.format_solution(best_solution)
        conflicts = optimizer.validate_assignment(best_solution)

        return jsonify({
            "success": True,
            "solution": formatted_solution,
            "statistics": {
                "total_assignments": len(formatted_solution),
                "conflicts": conflicts,
                "fitness_history": fitness_history,
                "best_fitness": max(fitness_history),
                "generations": len(fitness_history)
            }
        })

    except Exception as e:
        return jsonify({"error": f"Error en optimización: {str(e)}"}), 500
