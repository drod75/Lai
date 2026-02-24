import streamlit as st
from testing.utils.setup import presets
from src.utils.stt import speech_to_text
from pprint import pprint

presets()

audio = st.file_uploader("chose a file", type=["wav", "mp3", "m4a"])

if audio:
    transcription = st.session_state[
        "elevenlabs"
    ].speech_to_text.convert(
        file=audio,
        model_id="scribe_v2",  # Model to use
        tag_audio_events=True,  # Tag audio events like laughter, applause, etc.
        language_code="eng",  # Language of the audio file. If set to None, the model will detect the language automatically.
        diarize=True,  # Whether to annotate who is speaking
    )

    pprint(transcription)

    st.markdown(transcription)
