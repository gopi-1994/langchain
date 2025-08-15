import os
from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.schema import (AIMessage, HumanMessage, SystemMessage)
load_dotenv(dotenv_path="keys.env")



key = os.getenv("openai_api_key")
llm = OpenAI(
    model="gpt-4.1-nano-2025-04-14", #gpt-oss-120b
       api_key=os.getenv("openai_api_key"),
       
       )

# result = llm.invoke("give a python code for a factorial function")
# print(result)

# for chat model
    
chat = ChatOpenAI(
    model="gpt-4.1-nano-2025-04-14",
    api_key=os.getenv("openai_api_key")
    )
messages = [
    SystemMessage(content="You are a Senior staff software engineer with 10 years of expertise in python & Machine learning"),
    HumanMessage(content="Give the best ML algo to do the classification task")
]

response = chat.invoke(input=messages)
print(response)
    
    
#     base_url="https://router.huggingface.co/v1",
#     api_key=os.getenv("HF_KEY"),
# )

# completion = client.chat.completions.create(
#     model="openai/gpt-oss-120b:fireworks-ai",
#     messages=[
#         {
#             "role": "user",
#             "content": "What is the capital of France?"
#         }
#     ],
# )
# print(completion)
# res = client.responses.create(
#     model="openai/gpt-oss-120b:fireworks-ai",
#     input="hi",
#     )
# print(res)
# print("**" * 20)
# print(completion.choices[0].message.content)
