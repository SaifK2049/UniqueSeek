import ollama 
from fastapi import FastAPI
app = FastAPI()

@app.get("/generate/")
def generate(prompt: str):
    response = ollama.chat(model="deepseek-coder", messages=[{"role": "user", "content": prompt}])
    return {"response": response['message']['content']}
