import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from embedchain import App

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = "sk-proj-DcyLBsh9VEJOO3FA0z8oT3BlbkFJ8fapY6I9kNlIyO3UNRWo"


app = FastAPI(title="Chatbot API")

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize Embedchain app with data
embedchain_app = App()
embedchain_app.add('commercial_books_law_formatted.txt')

# Request and Response Models
class Message(BaseModel):
    text: str

class ResponseModel(BaseModel):
    response: str

@app.post("/chat/", response_model=ResponseModel)
async def chat(message: Message):
    try:
        response_text = embedchain_app.query(message.text)
        return ResponseModel(response=response_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"Welcome": "This is a simple chatbot API. Send POST requests to /chat/"}

