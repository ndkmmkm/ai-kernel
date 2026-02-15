from flask import Flask, request, jsonify
from loader import load_core

app = Flask(__name__)
ai = load_core()

@app.route("/")
def health():
    return "Kernel is alive."

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json or {}
    message = data.get("message", "")
    reply = ai.respond(message)
    return jsonify({"reply": reply})
