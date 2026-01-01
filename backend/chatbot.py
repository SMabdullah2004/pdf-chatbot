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

    # Split text into chunks (larger size for more context)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    documents = splitter.create_documents([text])

    # Embeddings (more accurate model)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )

    # Build vector DB
    vector_db = FAISS.from_documents(documents, embeddings)

    # HuggingFace text-generation pipeline
    llm_pipeline = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        max_length=512
    )


def get_chatbot_response(query: str) -> str:
    if vector_db is None or llm_pipeline is None:
        return "Please upload a PDF first."

    # Fetch top 5 chunks for better coverage
    docs = vector_db.similarity_search(query, k=5)
    if not docs:
        return "No relevant information found in the uploaded PDF."

    context = "\n".join([doc.page_content for doc in docs])

    # Detailed RAG-style prompt
    prompt = f"""
You are an expert assistant. Answer the question ONLY based on the context below from the uploaded PDF.
Do NOT invent information. Combine relevant details from all retrieved chunks to give a clear, detailed, and accurate answer.

Context:
{context}

Question:
{query}
"""

    # Generate answer
    result = llm_pipeline(prompt)
    return result[0]['generated_text'].strip()
