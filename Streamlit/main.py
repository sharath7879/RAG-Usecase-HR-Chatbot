import streamlit as st
from langchain_community.llms import CTransformers
from langchain_community.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.chains import RetrievalQA
from langchain.chains import VectorDBQAWithSourcesChain
from langchain_community.output_parsers.rail_parser import GuardrailsOutputParser
import os


# Create llm for response
llm=CTransformers(model='models/llama-2-7b-chat.Q8_0.gguf',
                  model_type='llama',
                  config={'max_new_tokens':200,
                         'temperature':0.01,
                         'context_length': 2000})


#extract embeddings
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

persistent_directory = 'db_files'

db = Chroma(persist_directory=persistent_directory, embedding_function=embeddings)


def generate_response(query_text):
         #qa = VectorDBQAWithSourcesChain.from_chain_type(llm=llm, k=1, chain_type="stuff", vectorstore=db)
         retriever = db.as_retriever()
         qa = RetrievalQA.from_chain_type(llm, chain_type='stuff', retriever=retriever)
         return qa.invoke(query_text)


# Page title
st.set_page_config(page_title='🦜🔗 F5 HR Chatbot')
st.title('🦜🔗 F5 HR Chatbot')

# Query text
query_text = st.text_input('Enter your question:', placeholder = 'Please provide a short summary.')

# Form input and query
result = []
with st.form('my_form', clear_on_submit=True):
  submitted = st.form_submit_button('Submit')
  if submitted:
    response = generate_response(query_text)
    result.append(response)

if len(result):
    st.info(response)
