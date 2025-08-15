import os
from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import OpenAI
load_dotenv(dotenv_path="keys.env")



key = os.getenv("openai_api_key")
llm = OpenAI(model="gpt-4.1-nano-2025-04-14",
       api_key=os.getenv("openai_api_key"))

result = llm.invoke("give a python code for a factorial function")
print(result)
    
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
