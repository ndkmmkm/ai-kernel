from classifier import classify
from llm import generate_response
from responses import refusal_template

@app.post("/ask")
def ask():
    user_input = request.json["message"]

    risk = classify(user_input)

    if risk["action"] == "refuse":
        return refusal_template(risk)

    llm_output = generate_response(user_input)

    return wrap_schema(llm_output)
