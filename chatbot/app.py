from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")

if not openai_api_key:
    st.error("OPENAI_API_KEY is not set!")
if not langchain_api_key:
    st.error("LANGCHAIN_API_KEY is not set!")

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# PROMPT TEMPLATE
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a renown poet - Sylvia Plath. Please write a 2-line poem about the user's queries"),
        ("user", "Question:{question}")
    ]
)

# streamlit framework

st.title('Let me write a poem for you')
input_text = st.text_input("What do you want the poem to be about?")

# openAI LLm
llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
