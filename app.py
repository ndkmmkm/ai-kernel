print("BOOT: app.py loaded")

from flask import Flask, request, jsonify
print("BOOT: flask imported")


from flask import Flask, request, jsonify
from loader import load_core
from kernel.state import get_session, SessionState
from kernel.trust import update_trust
from kernel.degrade import degrade_response
import os


print("BOOT: about to start server")

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
    trust = update_trust(session, message)

    try:
        reply = ai.respond(message)
    except Exception:
        reply = "Session unavailable."

    reply = degrade_response(reply, trust)
    return jsonify({"reply": reply})

@app.route("/_internal/test", methods=["POST"])
def internal_test():
    payload = request.json or {}
    message = payload.get("message", "")

    fake_session = SessionState()
    fake_session.learning_enabled = True

    try:
        reply = ai.respond(message)
    except Exception as e:
        reply = f"internal error: {e}"

    return jsonify({
        "reply": reply,
        "shadow": {
            "learning_enabled": fake_session.learning_enabled,
            "trust": fake_session.trust
        }
    })

print("BOOT: about to bind port")

port = int(os.environ.get("PORT", 3000))
app.run(host="0.0.0.0", port=port)





