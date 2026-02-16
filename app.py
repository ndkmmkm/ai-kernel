from flask import Flask, request, jsonify
from loader import load_core

app = Flask(__name__)
ai = load_core()

@app.route("/")
def health():
    return "nigga is you slow or what."

@app.route("/ask")

@app.route("/ask")
def ask():
    reply = ai.respond("test")
    return reply

