import streamlit as st
from testing.utils.setup import presets
from pprint import pprint
from src.agent.agent import agent_pipeline
from dotenv import load_dotenv

with st.spinner("Loading presets...", show_time=True):
    load_dotenv()
    presets()
st.success("Done loading presets!", icon="✅")

with st.spinner("Creating agent...", show_time=True):
    st.session_state["lai"] = agent_pipeline(
        provider="Google", model_type="gemini-2.5-flash"
    )
st.success("Done creating agent!", icon="✅")

st.markdown("# Transcript Test 2")
c1, c2, c3 = st.columns(3)
with c1:
    st.header("Text Option")
    st.session_state["last_entry"] = st.text_input("Transcript goes here!")

with c2:
    st.header("Recording Option")
    audio = st.audio_input("Record you're conversation!")
    st.session_state["last_entry"] = st.session_state[
        "elevenlabs"
    ].speech_to_text.convert(
        file=audio,
        model_id="scribe_v2",  # Model to use
        tag_audio_events=True,  # Tag audio events like laughter, applause, etc.
        language_code="eng",  # Language of the audio file. If set to None, the model will detect the language automatically.
        diarize=True,  # Whether to annotate who is speaking
    )

with c3:
    st.header("Audio File Option")
    audio = st.file_uploader("Choose an audio file!", type=["wav", "mp3", "m4a"])
    st.session_state["last_entry"] = st.session_state[
        "elevenlabs"
    ].speech_to_text.convert(
        file=audio,
        model_id="scribe_v2",  # Model to use
        tag_audio_events=True,  # Tag audio events like laughter, applause, etc.
        language_code="eng",  # Language of the audio file. If set to None, the model will detect the language automatically.
        diarize=True,  # Whether to annotate who is speaking
    )

if st.session_state["last_entry"]:
    with st.spinner("Awaiting response...", show_time=True):
        temporary_response = st.session_state["lai"].invoke(
            {"messages": [{"role": "user", "content": st.session_state["last_entry"]}]}
        )
        st.session_state["last_response"] = temporary_response["messages"][-1].content[
            -1
        ]["text"]

    st.markdown(st.session_state["last_response"])
