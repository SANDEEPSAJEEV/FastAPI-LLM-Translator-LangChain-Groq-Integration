from fastapi import FastAPI 
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage 
from langserve import add_routes
import os
from dotenv import load_dotenv  
load_dotenv()  # Load environment variables from .env file


groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(model_name="gemma2-9b-it", api_key=groq_api_key)


#1.create a prompt template
generic_prompt = "Translate the following into French: {language}"
prompt = ChatPromptTemplate.from_messages([("system", generic_prompt), ("user", "{text}")]) 


#2.create an output parser
parser= StrOutputParser()

#3.chain the components
chain = prompt | model | parser

#4.App definition

app = FastAPI(title='LangChain server', description='A simple API server using LangChain with Groq for fast inferencing', version='0.1.0')


## 5.Adding chain routes
add_routes(app, chain, path="/groq")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000, log_level="info")