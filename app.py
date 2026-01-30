from flask import Flask, request, jsonify
from loader import load_core

app = Flask(__name__)
ai = load_core()

@app.route("/")
def health():
    return "AI kernel running"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json or {}
    message = data.get("message", "")

    try:
        reply = ai.respond(message)
    except Exception:
        reply = "Session unavailable."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
