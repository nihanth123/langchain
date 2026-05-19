from dotenv import load_dotenv

import os

load_dotenv()
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
from tavily import TavilySearch


tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def search(query: str) -> str:
    """Tool that searches over internet
    Args:
         query: The query to search for
    Returns:
          The search result   
    """
    print(f"Searching for {query}")
    return tavily.search(query = query)

#llm = ChatOllama(model="gemma4:e4b", temperature=0.2, streaming=False )
llm = ChatOpenAI(model="gpt-5")

tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain agents")
    result = agent.invoke({"messages": [HumanMessage(content="Search for three AI engineer job postings in Denver, Colorado and list their details.")]})
    print(result)

if __name__ == "__main__":
    main()