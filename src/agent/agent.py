import streamlit as st
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Literal
from src.agent.tools.tools import give_tools


@st.cache_resource
def create_model(
    provider: Literal["Google", "Ollama"],
    model_type: Literal["llama3.2:1b", "llama3.2:3b", "gemma3:4b"],
):
    if provider == "Google":
        model = ChatGoogleGenerativeAI(model="gemini-3-flash")
        return model
    else:
        model = ChatOllama(model=model_type, temperature=0.4)
        return model


@st.cache_resource
def create_prompt():
    pass


@st.cache_resource
def create_agent(
    provider: Literal["Google", "Ollama"],
    model_type: Literal["llama3.2:1b", "llama3.2:3b", "gemma3:4b"],
):
    model = create_model(provider, model_type)
    system_prompt = create_prompt()
    tools = give_tools()
    agent = create_agent(model, tools=tools, system_prompt=system_prompt)  # type: ignore

    return agent
