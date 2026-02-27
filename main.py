from fastapi import FastAPI
from pydantic import BaseModel
from llm import generate_response

app = FastAPI()

class Message(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"status": "Kernel is running"}

@app.post("/chat")
def chat(message: Message):
    response = generate_response(message.prompt)
    return {"response": response}
