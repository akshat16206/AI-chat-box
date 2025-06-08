from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv() # this is gonna load the enviorment file (.env) 

# LLM setup
#llm = ChatOpenAI(model = "gpt-3.5-turbo", api_key="")   if we want to use open ai
llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")


