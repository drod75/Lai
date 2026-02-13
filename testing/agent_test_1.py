"""
IMPORTANT!!!

This file if you want to test it, needs to be moved to the main folder, to avoid relative importing issues.
"""

from src.agent.agent import agent_pipeline
from src.utils.stt import speech_to_text
import streamlit as st
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
import os


@st.cache_resource
def load_env():
    load_dotenv()


@st.cache_resource
def agent():
    agent = agent_pipeline(provider="Google", model_type="gemini-2.5-flash")
    return agent


@st.cache_resource
def load_elevenlabs():
    elevenlabs = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
    )

    if "elevenlabs" not in st.session_state:
        st.session_state["elevenlabs"] = elevenlabs


load_env()
load_elevenlabs()
st.session_state["lai"] = agent()

st.set_page_config(
    page_title="Lai Test 1",
    page_icon="⚠️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.header("Agent Test 1")

audio_value = st.audio_input("Record high quality audio!", sample_rate=48000)
st.audio(audio_value)

with st.expander("Speech to Text Test!"):
    if audio_value:
        transcript = speech_to_text(audio_value)
        result = st.session_state["lai"].invoke(
            {"messages": [{"role": "user", "content": transcript}]}
        )

        st.markdown(result["messages"][-1].content[-1]["text"])

    else:
        st.warning("No audio yet! :(")
