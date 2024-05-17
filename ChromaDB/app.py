from langchain_community.document_loaders import TextLoader,PyPDFLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
import os
import time


# Directory to save downloaded files
download_dir = 'downloads'

# Persistent directory to store the vector data
persistent_directory = 'db_files'

#extract embeddings
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Track downloaded files
downloaded_files = set()

def doc_split():
       for file_name in os.listdir(download_dir):
              # Get the full path of the file
              file_path = os.path.join(download_dir, file_name)
              if file_name not in downloaded_files:
                     if file_name.endswith('.txt'):
                            document = TextLoader(file_path).load()
                            downloaded_files.add(file_name)
                     if file_name.endswith('.pdf'):
                            document = PyPDFLoader(file_path).load()
                            downloaded_files.add(file_name)      
                     # Split documents into chunks
                     text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
                     texts = text_splitter.split_documents(document)
                     #vector store with metadata
                     vectordb = Chroma.from_documents(texts,embeddings, persist_directory=persistent_directory )
                     vectordb.persist()
       
while True:
       doc_split()
       time.sleep(60)   



