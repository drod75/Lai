import streamlit as st
import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs


@st.cache_resource
def load_env():
    load_dotenv()


@st.cache_resource
def load_elevenlabs():
    elevenlabs = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
    )

    if "elevenlabs" not in st.session_state:
        st.session_state["elevenlabs"] = elevenlabs


def presets():
    load_env()
    load_elevenlabs()

    st.set_page_config(
        page_title="Lai Test 1",
        page_icon="⚠️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
