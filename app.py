from memory import add_interaction
from flask import Flask, request, jsonify
from loader import load_core
import logging
from kernel.router import process   # ← move import to top

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
ai = load_core()

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json or {}
    message = data.get("message", "")

    logger.info(f"Incoming message: {message}")

    reply = process(message)

    add_interaction(message, reply)

    logger.info(f"Outgoing reply: {reply}")

    return jsonify({"reply": reply})
