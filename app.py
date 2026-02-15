from flask import Flask, request, jsonify
from fake_core import get

app = Flask(__name__)
ai = get()

@app.route("/")
def health():
    return "Kernel is alive."

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json or {}
    message = data.get("message", "")
    reply = ai.respond(message)
    return jsonify({"reply": reply})
    
