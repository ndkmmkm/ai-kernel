from fastapi import FastAPI
from pydantic import BaseModel
from LLM import generate_response

app = FastAPI()

class Message(BaseModel):
    prompt: str

@app.post("/chat")
def chat(message: Message):
    response = generate_response(message.prompt)
    return {"response": response}
