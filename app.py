from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "PayWave Payment API",
        "status": "Running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "Healthy"})
