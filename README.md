# 📄 AI PDF Chatbot

An AI-powered chatbot that answers questions **only based on the content of an uploaded PDF** using **RAG (Retrieval-Augmented Generation)**.

Built with:

- **FastAPI** – backend REST API
- **HuggingFace Transformers** – LLM
- **LangChain** – text splitting & embeddings
- **FAISS** – vector database for similarity search
- **HTML/CSS/JS** – responsive frontend

---

## 🏆 Features

- Upload a PDF and automatically build a knowledge base.
- Ask questions and receive answers **grounded only in the uploaded PDF**.
- Accurate RAG-style answers: no fabricated information.
- Dark-themed, responsive, animated chat interface.
- FastAPI backend with REST API for easy integration.
- Fully containerized with **Docker** for deployment.

---

## 📂 Project Structure

pdf-chatbot/
│
├── backend/
│ ├── main.py # FastAPI endpoints
│ ├── chatbot.py # PDF RAG logic & embeddings
│ └── pdf_utils.py # PDF text extraction
│
├── frontend/
│ ├── index.html # Chat interface
│ ├── style.css # Styling
│ └── script.js # JS for chat interactions
│
├── requirements.txt # Python dependencies
├── Dockerfile # Docker container setup
└── README.md # Project documentation


---

## 1️⃣ Prerequisites

- Python 3.11+ → [Download](https://www.python.org/downloads/)
- Git → [Download](https://git-scm.com/downloads)
- Docker → [Download](https://www.docker.com/products/docker-desktop)
- Browser for frontend (Chrome, Edge, Firefox, etc.)

---

## 2️⃣ Clone Repository

```bash
git clone https://github.com/SMabdullah2004/pdf-chatbot.git
cd pdf-chatbot

3️⃣ Setup Python Virtual Environment (Optional but Recommended)
python -m venv venv

Activate Virtual Environment

Windows PowerShell:

.\venv\Scripts\Activate.ps1


Windows CMD:

.\venv\Scripts\activate.bat


Linux/macOS:

source venv/bin/activate

4️⃣ Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt


Dependencies include: FastAPI, uvicorn, PyPDF2, transformers, torch, FAISS, LangChain, sentence-transformers, python-multipart.

5️⃣ Run Backend (FastAPI)
uvicorn backend.main:app --reload


API will be available at http://127.0.0.1:8000

Swagger docs at http://127.0.0.1:8000/docs

6️⃣ Run Frontend
Option 1 – Open HTML Directly

Navigate to frontend/

Open index.html in your browser

Upload PDF → Ask questions → Answers appear PDF-grounded

Option 2 – Serve via Local Server
cd frontend
python -m http.server 5500


Access frontend at http://localhost:5500

7️⃣ Using the Chatbot

Click Upload PDF → Wait for "PDF Uploaded Successfully"

Type your question → Click Send

Answers are strictly based on PDF content and combine top relevant chunks

Chatbox auto-scrolls for new messages

8️⃣ API Endpoints
Endpoint	Method	Description
/	GET	Check API status
/upload	POST	Upload PDF & create knowledge base
/chat	POST	Ask a question and get PDF-based answer
Example /chat Request
{
  "question": "What is the main topic of the PDF?"
}

Example /chat Response
{
  "answer": "The PDF explains how to build an AI PDF chatbot using FastAPI, LangChain, and FAISS..."
}

9️⃣ Docker Setup
Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]

Build Docker Image
docker build -t pdf-chatbot .

Run Docker Container
docker run -d -p 8000:8000 --name pdf-chatbot-container pdf-chatbot


Backend URL: http://localhost:8000

Frontend: Open index.html or serve via local server

Stop / Remove Container
docker ps
docker stop pdf-chatbot-container
docker rm pdf-chatbot-container

🔟 GitHub Version Control
Initialize Repository
git init
git add .
git commit -m "Initial commit: PDF Chatbot project"

Add Remote & Push
git remote add origin https://github.com/SMabdullah2004/pdf-chatbot.git
git branch -M main
git push -u origin main

🎨 Frontend Styling Notes

Dark blue + white theme

Responsive chat interface

Smooth button hover animations

Auto-scroll chatbox for new messages