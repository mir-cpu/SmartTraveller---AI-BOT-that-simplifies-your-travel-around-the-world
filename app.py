from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.callbacks.tracers import LangChainTracer
from langchain.callbacks.manager import CallbackManager
from langchain_community.llms import Ollama



import streamlit as st
import os
from dotenv import load_dotenv



load_dotenv()
print(os.getenv("LANGCHAIN_PROJECT"))
prompt = ChatPromptTemplate.from_messages(
    [("system","You are a helpful assistant who answers the users queries politely"),
     ("user","{query}")
      ]
)

##Visual end of the chatbot

st.title("Ask your all your travel queries ✈️!")
user_input = st.text_input("Search aiports, food, rented cars.....")
##tracking and monitoring
#tracker = LangChainTracer("chatbot_v1")
# monitor  = CallbackManager([tracker])
##setting the llm model
llm = Ollama(model="llama2:7b")

if user_input:
    formatted_input = prompt.format(query=user_input)
    response = llm.generate([formatted_input]).generations[0][0].text
    st.write(response)

