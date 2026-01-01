# main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pdf_utils import extract_text_from_pdf  # Make sure this exists
from chatbot import create_knowledge_base, get_chatbot_response

app = FastAPI()

# Enable CORS so frontend can call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Allow all origins (or specify your frontend)
    allow_methods=["*"],       # Allow all HTTP methods
    allow_headers=["*"],       # Allow all headers
)

# Upload PDF and create knowledge base
@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    # Extract text from PDF using your utility
    text = await extract_text_from_pdf(file)
    
    # Create embeddings and initialize chatbot
    create_knowledge_base(text)
    
    return {"message": "PDF uploaded and knowledge base created."}

# Chat endpoint
@app.post("/chat")
async def chat(query: dict):
    # Get answer from chatbot
    answer = get_chatbot_response(query["question"])
    return {"answer": answer}

# Root endpoint to verify server is running
@app.get("/")
def home():
    return {"message": "PDF Chatbot API is running"}
