from src.helper import load_pdf,text_split,downloading_embeddingmodel
from langchain.vectorstores import Pinecone
import pinecone
from pinecone import Pinecone
from dotenv import load_dotenv
import os

load_dotenv()
key=os.environ.get('Pine_cone_api_keys')
print(key)

pc=Pinecone(api_key=key)
Indexname="medicalchatbot"
index=pc.Index(Indexname)
print(index.describe_index_stats())