import uuid
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.schema import (AIMessage, HumanMessage, SystemMessage)
from langchain.prompts import PromptTemplate
from pinecone import Pinecone, ServerlessSpec

from langchain.text_splitter import RecursiveCharacterTextSplitter



load_dotenv(dotenv_path="keys.env")
key = os.getenv("openai_api_key")
pinecone_key = os.getenv("pinecone_api_key")


llm = ChatOpenAI(
    model="gpt-4.1-nano-2025-04-14",
    api_key=key
    )

embedding_llm = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=key
    )

pc = Pinecone(
    api_key=pinecone_key,
    environment="us-west1-gcp"  # Adjust based on your Pinecone environment
)
index_name = "embedding-index"
dimension = 1536  # Adjust based on the embedding model used

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=dimension,
        spec=ServerlessSpec(cloud="aws", region="us-east-1")       
    )

# Connect to index
index = pc.Index(index_name)
# for chat model
    
messages = [
    SystemMessage(content="You are a Senior staff software engineer with 10 years of expertise in python & Machine learningin 500 words"),
    HumanMessage(content="Give the best ML algo to do the classification task")
]


template = """"You are a helpful assistant. Answer the question based on the context provided in 500 words.
Question: {question}"""
prompt = PromptTemplate(input_variables=["question"], template=template)
chain = prompt | llm

# ********************************************

## run one time form embidding the answer
# res = chain.invoke({"question": "What is the Nvidia top gpu ?"})
# to embed chunks into page content and upsert

# text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=80)
# texts = text_splitter.create_documents([res.content])
# chunks = [doc.page_content for doc in texts]
# vectors = embedding_llm.embed_documents(chunks)
# to_upsert = [
#     (str(i), vec, {"chunk": chunks[i]})
#     for i, vec in enumerate(vectors)
#     ]
# index.upsert(
#     vectors=to_upsert,
#     namespace="default"
# )

# ********************************************

query2 ="What is the Nvidia top gpu ?"
emb_query = embedding_llm.embed_query(query2)

ress = index.query(vector=emb_query, top_k=10, include_metadata=True, namespace="default")
context = [item['metadata']['chunk'] 
           if 'chunk' in item['metadata'] 
           else "No context found" 
           for item in ress['matches']]

template2 = """"You are a helpful assistant. Answer the question based on the context provided.
Question: {question}, 
Context: {context}
"""
prompt2 = PromptTemplate(input_variables=["question", "context"], template=template2)
chain = prompt2 | llm
res2 = chain.invoke({"question": query2, "context": context})
print(res2.content)





