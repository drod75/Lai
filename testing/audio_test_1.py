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


load_env()
load_elevenlabs()

st.set_page_config(
    page_title="Lai Test 1",
    page_icon="⚠️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.header("Audio Test 1")

audio_value = st.audio_input("Record high quality audio!", sample_rate=48000)
st.audio(audio_value)

with st.expander("Speech to Text Test!"):
    if audio_value:
        st.markdown(type(audio_value))
        transcription = st.session_state["elevenlabs"].speech_to_text.convert(
            file=audio_value,
            model_id="scribe_v2",
            tag_audio_events=True,
            language_code="eng",
            diarize=True,
        )
        st.markdown(type(transcription))
        st.markdown(transcription.text)

    else:
        st.warning("No audio yet! :(")
