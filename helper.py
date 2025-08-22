from dotenv import load_dotenv
import os
import json
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate


load_dotenv(dotenv_path="keys.env")
key = os.getenv("openai_api_key")

llm = ChatOpenAI(
    # model="gpt-5",
    model="gpt-4.1-nano-2025-04-14",
    api_key=key
)
 

def generate_restaurant_name_and_items(cusine):
    prompt = PromptTemplate(
    input_variables=["cusine"],
    template="""I want to open a restaurant for {cusine} food, Suggest a fancy name & food itmes for this.
    output name format in JSON object with restaurant_name and menu_items as keys.
    For Example: {{"restaurant_name": "Curry Delight", "menu_items": "samosa, butter_chicken, naan"}}
    """
    )
    chain = prompt | llm
    result = chain.invoke({"cusine": cusine})
    content = result.content.strip()
    sj = json.loads(content)  # Ensure the content is valid JSON
    print(sj)
    
   
    return{
        "restaurant_name": sj.get("restaurant_name", "Default Restaurant Name"),
        "menu_items": sj.get("menu_items", "Default Menu Items")
    }