import os
from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.schema import (AIMessage, HumanMessage, SystemMessage)
from langchain.prompts import PromptTemplate



load_dotenv(dotenv_path="keys.env")
key = os.getenv("openai_api_key")

# for chat model
    
llm = ChatOpenAI(
    model="gpt-4.1-nano-2025-04-14",
    api_key=key
    )
messages = [
    SystemMessage(content="You are a Senior staff software engineer with 10 years of expertise in python & Machine learning"),
    HumanMessage(content="Give the best ML algo to do the classification task")
]


template = """"You are a helpful assistant. Answer the question based on the context provided.
Question: {question}"""
prompt = PromptTemplate(input_variables=["question"], template=template)
chain = prompt | llm
res = chain.invoke({"question": "What is the Nvidia top gpu ?"})
print(res)

