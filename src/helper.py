from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DirectoryLoader,PyMuPDFLoader,PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings


# Extract data from pdf
def load_pdf(data):
    loader=DirectoryLoader(data,glob="*.pdf",loader_cls=PyPDFLoader)

    documents=loader.load()

    return documents

#create text chucks 
def text_split(extracted_data):

    text_splitter= RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks= text_splitter.split_documents(extracted_data)

    return text_chunks

# Download embedding model
def downloading_embeddingmodel():
    embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings
