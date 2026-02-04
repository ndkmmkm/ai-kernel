from flask import Flask, request, jsonify
from loader import load_core

from kernel.state import get_session
from kernel.trust import update_trust
from kernel.degrade import degrade_response

app = Flask(__name__)
ai = load_core()

@app.route("/")
def health():
    return "AI kernel running"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json or {}
    message = data.get("message", "")
    client_id = request.remote_addr  # simple for now

    session = get_session(client_id)
    trust = update_trust(session, message)

    try:
        reply = ai.respond(message)
    except Exception:
        reply = "Session unavailable."

    reply = degrade_response(reply, trust)
    return jsonify({"reply": reply})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)


