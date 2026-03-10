import os
from dotenv import load_dotenv
# from langchain_google_community import BigQueryVectorStore
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI

from rag import RAGProcessor

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
PROJECT_ID = os.getenv("PROJECT_ID")
DATASET = os.getenv("DATASET")
REGION = os.getenv("REGION")
TABLE = os.getenv("TABLE")

embedding_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001",
                                               api_key=API_KEY,
                                               vertexai=False,
                                               project=PROJECT_ID)

# vector_store = BigQueryVectorStore(
#     project_id=PROJECT_ID,
#     dataset_name=DATASET,
#     table_name=TABLE,
#     location=REGION,
#     embedding=embedding_model
# )

vector_store = InMemoryVectorStore(embedding=embedding_model)

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",
                             api_key=API_KEY,
                             vertexai=False,
                             project=PROJECT_ID,
                             location=REGION)

rag = RAGProcessor(vector_store, llm)

print("RAG Processor initialized successfully.")

print("Loading document...")
document_path = "https://arxiv.org/pdf/2410.16908.pdf"
print(f"Document path: {document_path}")
documents = rag.load_pdf_doc(document_path)
print(f"Loaded {len(documents)} document(s).")

print("Splitting document into chunks...")
doc_chunks = rag.split_doc_to_chunks(documents)
print(f"Split into {len(doc_chunks)} chunks.")

print("Embedding and storing document chunks in vector store...")
rag.embed_and_store(doc_chunks)
print("Document chunks embedded and stored successfully.")

# take query from the user input in loop unless user say stop
while True:
    user_input = input("\nEnter your query (or type 'stop' to exit): ")
    if user_input.lower() == 'stop':
        print("Exiting...")
        break
    query = user_input

    print(f"Retrieving data from vector store for query: '{query}'")
    relevant_docs = rag.retrieve_data_from_vector_store(query)

    context = "\n".join([doc.page_content for doc in relevant_docs])
    print("Generating answer using LLM...")
    answer = rag.generate_answer(context, query)
    print("Answer:")
    print(answer)

print("RAG process completed.")
