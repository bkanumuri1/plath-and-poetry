from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory
from langchain.chains import LLMChain

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

# streamlit framework

st.title('Let me write a poem for you')
input_text = st.text_input("What do you want the poem to be about?")

# setup memory for prompts
messages = StreamlitChatMessageHistory()
memory = ConversationBufferMemory(chat_memory=messages, return_messages=True)

# PROMPT TEMPLATE
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a renowned poet - Sylvia Plath. Based on previous themes, write a 2-line poem about the user's latest query"),
        ("user", "Question:{question}")
    ]
)


# openAI LLm
llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)
chain = LLMChain(llm=llm, prompt=prompt, memory=memory, verbose=True)

if input_text:
    result = chain.run(question=input_text)
    st.write(result)
