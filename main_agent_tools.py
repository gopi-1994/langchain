from dotenv import load_dotenv
import os
import json
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import AgentType, initialize_agent
from langchain_community.agent_toolkits.load_tools import load_tools


load_dotenv(dotenv_path="keys.env")
key = os.getenv("openai_api_key")

llm = ChatOpenAI(
    # model="gpt-5",
    model="gpt-4.1-nano-2025-04-14",
    api_key=key
)

tools = load_tools(["wikipedia"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
res = agent.invoke("Explain algebra in simple terms")
print(res)





