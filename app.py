from flask import Flask, request, jsonify
from loader import load_core
from kernel.state import get_session
from kernel.trust import update_trust
from kernel.degrade import degrade_response
from kernel.stress import stress_classify
import os

app = Flask(__name__)
ai = load_core()

@app.route("/")
def health():
    return "AI kernel running"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json or {}
    message = data.get("message", "")
    client_id = request.remote_addr

    session = get_session(client_id)

    # stress classification per request
    stress_flags = stress_classify(message)

    trust = update_trust(session, message, stress_flags)

    try:
        reply = ai.respond(message)
    except Exception:
        reply = "Session unavailable."

    reply = degrade_response(reply, trust, stress_flags)

    return jsonify({
        "reply": reply,
        "stress": stress_flags
    })

port = int(os.environ.get("PORT", 3000))
app.run(host="0.0.0.0", port=port)
