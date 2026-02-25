import streamlit as st
import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from src.utils.stt import speech_to_text
from src.agent.agent import agent_pipeline
from src.utils.agent_call import call

if "last_entry" not in st.session_state:
    st.session_state["last_entry"] = None
if "last_response" not in st.session_state:
    st.session_state["last_response"] = None

load_dotenv()

@st.cache_resource
def get_elevenlabs_client():
    return ElevenLabs(api_key=st.secrets["ELEVENLABS_API_KEY"])

@st.cache_resource
def get_ai_agent():
   return agent_pipeline(
        provider="google_genai", 
        model="gemini-2.5-flash"
    )

st.session_state["elevenlabs"] = get_elevenlabs_client()
st.session_state["agent"] = get_ai_agent()

st.markdown(
    '<div style="text-align: center"><h1>Lai 🤖</h1></div>', unsafe_allow_html=True
)
st.markdown(
    '<div style="text-align: center"><p style="font-style: italic; font-weight: bold;">To create a world where people on an influential platform can not lie to the world.</p></div>',
    unsafe_allow_html=True,
)


c1, c2, c3 = st.columns(3, border=True)

with c1:
    st.header("Text Option")
    text_input = st.text_input("Transcript goes here!", key="text_in")
    if text_input and text_input != st.session_state["last_entry"]:
        st.session_state["last_entry"] = text_input

with c2:
    st.header("Recording Option")
    audio_record = st.audio_input("Record your conversation!")
    if audio_record:
        st.session_state["last_entry"] = speech_to_text(audio_record)

with c3:
    st.header("Audio File Option")
    audio_file = st.file_uploader("Choose an audio file!", type=["wav", "mp3", "m4a"])
    if audio_file:
        st.session_state["last_entry"] = speech_to_text(audio_file)

if st.session_state["last_entry"] and not st.session_state["last_response"]:
    with st.spinner("Awaiting response..."):
        st.session_state["last_response"] = call(st.session_state["last_entry"])

with st.container(border=True):
    st.header("Lai Response")

    if st.session_state["last_response"]:
        st.markdown(st.session_state["last_response"])
    else:
        st.info("No current response available, please try on of the options above!")
