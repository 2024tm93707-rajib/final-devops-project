from flask import Flask, jsonify, request
from fitness_service import calculate_bmi

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "ACEest Fitness API",
        "status": "running"
    })

@app.route("/bmi", methods=["POST"])
def bmi():
    data = request.json
    weight = data.get("weight")
    height = data.get("height")

    bmi_value = calculate_bmi(weight, height)

    return jsonify({
        "bmi": bmi_value
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
