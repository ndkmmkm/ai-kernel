from flask import Flask, request, jsonify
from kernel.router import process

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    message = data.get("message")

    reply = process(message)

    return jsonify({"reply": reply})
