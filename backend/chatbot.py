# chatbot.py
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline

# Global variables
vector_db = None
llm_pipeline = None


def create_knowledge_base(text: str):
    """
    Create embeddings and initialize the PDF-grounded chatbot
    """
    global vector_db, llm_pipeline

    # Split text into chunks (smaller chunks improve relevance)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )
    documents = splitter.create_documents([text])

    # Embeddings (accurate model)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )

    # Build vector DB
    vector_db = FAISS.from_documents(documents, embeddings)

    # HuggingFace text-generation pipeline
    llm_pipeline = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        max_length=256
    )


def get_chatbot_response(query: str) -> str:
    if vector_db is None or llm_pipeline is None:
        return "Please upload a PDF first."

    # Fetch top 5 relevant chunks
    docs = vector_db.similarity_search(query, k=5)
    if not docs:
        return "No relevant information found in the uploaded PDF."

    context = "\n".join([doc.page_content for doc in docs])

    # STRONG prompt for concise PDF-only answers
    prompt = f"""
You are an expert assistant. Answer the question using ONLY the content from the PDF below.
Do NOT add any information that is not in the PDF.
Be concise and precise. If the answer is not present, say "The PDF does not contain this information."

Context:
{context}

Question:
{query}

Answer:
"""

    # Generate answer
    result = llm_pipeline(prompt)
    return result[0]['generated_text'].strip()
