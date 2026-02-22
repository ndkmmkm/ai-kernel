from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "kernel v1 active"}

@app.post("/ask")
def ask():
    return {"message": "hello"}
