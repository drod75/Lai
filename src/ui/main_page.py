import streamlit as st
from src.utils.agent_call import call
from src.utils.stt import speech_to_text
from dotenv import load_dotenv
from src.agent.agent import agent_pipeline
from elevenlabs.client import ElevenLabs
import os


with st.spinner("Loading presets...", show_time=True):
    load_dotenv()
    
    elevenlabs = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
    )

    if "elevenlabs" not in st.session_state:
        st.session_state["elevenlabs"] = elevenlabs

    st.session_state['last_response'] = None
st.success("Done loading presets!", icon="✅")

with st.spinner("Creating agent...", show_time=True):
    st.session_state["lai"] = agent_pipeline(
        provider="Google", model_type="gemini-2.5-flash"
    )
st.success("Done creating agent!", icon="✅")

st.markdown(
    '<div style="text-align: center"><h1>Lai 🤖</h1></div>', unsafe_allow_html=True
)
st.markdown(
    '<div style="text-align: center"><p style="font-style: italic; font-weight: bold;">To create a world where people on an influential platform can not lie to the world.</p></div>',
    unsafe_allow_html=True,
)

st.info(
    "Welcome to Lai! To start, you can either, record a conversation, input an audio file, or type up some text!",
    icon="ℹ️",
)

c1,c2,c3 = st.columns(3, border=True)
with c1:
    st.header("Text Option")
    st.session_state["last_entry"] = st.text_input("Transcript goes here!")

with c2:
    st.header("Recording Option")
    audio = st.audio_input("Record you're conversation!")
    if audio:
        st.session_state['last_entry'] = speech_to_text(audio)

with c3:
    st.header("Audio File Option")
    audio =  st.file_uploader("Choose an audio file!", type=["wav", "mp3", "m4a"])
    if audio:
        st.session_state['last_entry'] = speech_to_text(audio)

if st.session_state['last_entry'] and not st.session_state['last_response']:
    with st.spinner("Awaiting response...", show_time=True):
        st.session_state['last_response'] = call(st.session_state['last_entry'])

if st.session_state['last_response']:  
    with st.container(border=True):
        st.header("Lai Response")
        st.markdown(st.session_state['last_response'])