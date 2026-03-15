from src.agent.agent import agent_pipeline
from elevenlabs.client import ElevenLabs
import streamlit as st


@st.cache_resource
def get_elevenlabs_client():
    return ElevenLabs(api_key=st.secrets["ELEVENLABS_API_KEY"])


@st.cache_resource
def get_ai_agent():
    return agent_pipeline(provider=st.secrets["PROVIDER"], model=st.secrets["MODEL"])
