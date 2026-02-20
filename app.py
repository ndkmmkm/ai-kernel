from flask import Flask, request, jsonify
from kernel.router import process

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    message = data.get("message", "")

  {"reply": "...LLM processed message..."}

    return jsonify({"reply": reply})
