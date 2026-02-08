from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate

class RAGProcessor:
    def __init__(self, vector_store, llm):
        self.vector_store = vector_store
        self.llm = llm

    def load_pdf_doc(self, doc_path):
        # Logic to load documents from the given paths
        loader = PyPDFLoader(doc_path)
        return loader.load()
    
    def split_doc_to_chunks(self, documents, chunk_size=400, chunk_overlap=10):
        # Logic to split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, 
                                              chunk_overlap=chunk_overlap)
        return text_splitter.split_documents(documents)
    
    def embed_and_store(self, doc_chunks):
        # Logic to embed document chunks and store them in the vector store
        self.vector_store.add_documents(doc_chunks)

    def retrieve_data_from_vector_store(self, query, k=5):
        # Logic to retrieve relevant documents from the vector store
        return self.vector_store.similarity_search(query, k=k)
    
    def generate_answer(self, context, question):
        # Logic to generate answer using the LLM
        prompt_template = PromptTemplate(
            input_variables=["context", "question"],
            template="""
                Context: {context}
                Question: {question}
                Answer:
                """,
        )

        chain = prompt_template | self.llm

        response = chain.invoke({
            "context": context,
            "question": question
        })

        return response.content