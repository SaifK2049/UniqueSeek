from fastapi import FastAPI, UploadFile, File, Depends
import ollama
import subprocess 

app = FastAPI()

# Store dataset and chat history in memory
dataset_content = ""
chat_history = []

@app.get("/API-check")
def check_model():
    captured = subprocess.run(['ollama', 'ps'], capture_output=True)
    return captured.stdout


@app.post("/upload-dataset/")
async def upload_dataset(file: UploadFile = File(...)):
    """Uploads a dataset and stores it in memory."""
    global dataset_content
    dataset_content = (await file.read()).decode("utf-8")
    return {"message": "Dataset uploaded successfully", "size": len(dataset_content)}


@app.post("/clear-dataset/")
async def clear_dataset():
    """Clears the uploaded dataset from memory."""
    global dataset_content
    dataset_content = ""
    return {"message": "Dataset cleared successfully"}


@app.post("/clear-history/")
async def clear_history():
    """Clears the conversation history from memory."""
    global chat_history
    chat_history = []
    return {"message": "Chat history cleared successfully"}


@app.get("/generate/")
def generate(prompt: str):
    """Generates a response with the dataset and chat history as context."""
    global dataset_content, chat_history

    full_prompt = f"{dataset_content}\n\nPrevious conversation:\n"
    for msg in chat_history:
        full_prompt += f"{msg['role']}: {msg['content']}\n"
    
    full_prompt += f"User: {prompt}"

    # Get response from Ollama
    response = ollama.chat(model="deepseek-r1", messages=[{"role": "user", "content": full_prompt}])

    # Store interaction in chat history
    chat_history.append({"role": "user", "content": prompt})
    chat_history.append({"role": "assistant", "content": response['message']['content']})

    return {"response": response['message']['content']}

