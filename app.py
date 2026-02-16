from flask import Flask, request, jsonify
from loader import load_core

app = Flask(__name__)
ai = load_core()

@app.route("/")
def health():
    return "ok evey things good i think wwe have a bit mmore to do but well get it done."

@app.route("/ask")

@app.route("/version"))
def version():
    reply = ai.respond("test")
    return {"version": "0.1.0"}

