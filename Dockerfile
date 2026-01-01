# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy backend and frontend files
COPY backend/ ./backend/
COPY frontend/ ./frontend/
COPY requirements.txt ./

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for FastAPI
EXPOSE 8000

# Set environment variable for FastAPI
ENV UVICORN_CMD="uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload"

# Default command to run FastAPI
CMD ["sh", "-c", "$UVICORN_CMD"]

Build Docker Image

Run this in your terminal (from project root):

docker build -t pdf-chatbot .


⚠️ Make sure Docker Desktop is installed and running.

3️⃣ Run Docker Container
docker run -d -p 8000:8000 --name pdf-chatbot-container pdf-chatbot


-p 8000:8000 maps container port 8000 to host port 8000

--name pdf-chatbot-container gives a name to your container

4️⃣ Access Application

Backend API: http://localhost:8000

Frontend: Open frontend/index.html in your browser (or later you can serve frontend via FastAPI static files or Nginx)

✅ Optional: Stop / Remove Container
docker stop pdf-chatbot-container
docker rm pdf-chatbot-container