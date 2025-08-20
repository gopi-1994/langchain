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

# for chat model
    
messages = [
    SystemMessage(content="You are a Senior staff software engineer with 10 years of expertise in python & Machine learningin 500 words"),
    HumanMessage(content="Give the best ML algo to do the classification task")
]


template = """"I want to open a restaurant for {cuisine} cuisine., Suggest a fancy name for this"""
prompt = PromptTemplate(input_variables=["cuisine"], template=template)
prompt.format(cuisine="Indian")
chain = prompt | llm
res = chain.invoke({"cuisine":"Indian"}, version="v2")
print(res)





