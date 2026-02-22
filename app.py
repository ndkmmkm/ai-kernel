from fastapi import FastAPI
from pydantic import BaseModel
from llm import generate_response

app = FastAPI()

class AskRequest(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/ask")
def ask(request: AskRequest):
    response = generate_response(request.prompt)
    return {"response": response}
