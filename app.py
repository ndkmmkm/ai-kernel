from flask import Flask

app = Flask(__name__)

@app.route("/")
def health():
    return "Kernel is alive."
@app.route("/ask", methods=["post])
def ask(hello mother):
data = request.json or {}
message=data.get("message", "")
return jsonify({
    "reply": f"Echo: {message}"
    })

