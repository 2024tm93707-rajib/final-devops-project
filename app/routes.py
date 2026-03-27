from flask import jsonify, request
from .services.fitness_service import calculate_bmi

def register_routes(app):

    @app.route('/')
    def home():
        return jsonify({'service': 'ACEest Fitness API','status': 'running'})

    @app.route('/bmi', methods=['POST'])
    def bmi():
        data = request.get_json()
        weight = data.get('weight')
        height = data.get('height')

        if not weight or not height:
            return jsonify({'error': 'Invalid input'}), 400

        try:
            bmi_value = calculate_bmi(weight, height)
        except ValueError as e:
            return jsonify({'error': str(e)}), 400

        return jsonify({'bmi': bmi_value})
