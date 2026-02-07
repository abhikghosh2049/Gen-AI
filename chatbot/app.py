from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# ✅ load environment variables FIRST
load_dotenv()

# ✅ optional safety checks
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found. Check your .env file")

# LangSmith tracing (optional)
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# ---------------- Prompt Template ----------------
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Question: {question}")
    ]
)

# ---------------- Streamlit UI ----------------
st.title("LangChain Demo with OpenAI API")
input_text = st.text_input("Search the topic you want")

# ---------------- LLM ----------------
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)