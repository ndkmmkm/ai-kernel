from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def health():
    return "Kernel is alive."

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json or {}
    message = data.get("message", "")
    return jsonify({
        "reply": f"Echo: {message}"
    })
