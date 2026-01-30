echo "# ai-kernel" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ndkmmkm/ai-kernel.git
git push -u origin main
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
    except:
        reply = "Session unavailable."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
import os
import sys
import time

def detect_environment():
    return {
        "replit": "REPL_ID" in os.environ,
        "youware": "YOUWARE_RUNTIME" in os.environ or "youware" in sys.platform.lower(),
        "railway": "RAILWAY_ENVIRONMENT" in os.environ,
        "local": True
    }

def allowed_environment():
    env = detect_environment()
    return env["railway"] or env["replit"] or env["youware"]

def graceful_exit(msg="Session ended."):
    print(msg)
    time.sleep(0.5)
    raise SystemExit
import os
from environment_check import allowed_environment

def authorized():
    core_key = os.environ.get("CORE_KEY")
    allowed = os.environ.get("ALLOWED_ENV")

    if not core_key or not allowed:
        return False

    if not allowed_environment():
        return False

    return True
class FakeAI:
    def respond(self, prompt):
        return "Demo mode active. Full intelligence unavailable."

def get():
    return FakeAI()
import base64
import types
from gatekeeper import authorized
from fake_core import get as fake_get
from environment_check import graceful_exit

def load_core():
    if not authorized():
        graceful_exit("Session inactive.")
        return fake_get()

    try:
        with open("real_core.enc", "r") as f:
            encoded = f.read()

        decoded = base64.b64decode(encoded).decode()
        module = types.ModuleType("real_core")
        exec(decoded, module.__dict__)
        return module.get()

    except Exception:
        return fake_get()
import base64

code = """
class RealAI:
    def respond(self, prompt):
        return f"Processed intelligently: {prompt}"

def get():
    return RealAI()
"""

flask
