"""
# Transcript Test 1

This test is designed to test how well an agent can do depending on the transcript provided, whether or not giving the ai an input of for example a cleaned and processed transcript will make a difference, and by how much.
"""
import streamlit as st
from testing.utils.setup import presets
from pprint import pprint
from src.agent.agent import agent_pipeline
from dotenv import load_dotenv

load_dotenv()
presets()
st.session_state["lai"] = agent_pipeline(
    provider="Google", model_type="gemini-2.5-flash"
)

audio = st.audio_input("say something!")
file = st.file_uploader("Choose an audio file!", type=["wav", "mp3", "m4a"])

if audio:
    transcript = st.session_state['elevenlabs'].speech_to_text.convert(
        file=audio,
        model_id="scribe_v2",  # Model to use
        tag_audio_events=True,  # Tag audio events like laughter, applause, etc.
        language_code="eng",  # Language of the audio file. If set to None, the model will detect the language automatically.
        diarize=True,  # Whether to annotate who is speaking
    )

    pprint(transcript.words, indent=2)

    processed_transcript = ""
    for w in range(len(transcript.words)):
        word = transcript.words[w]
        scribed = f"(Word {w}: {word.text}, Speaker: {word.speaker_id})"
        processed_transcript += scribed 
    pprint(processed_transcript)

    st.markdown(processed_transcript)
    result = st.session_state["lai"].invoke(
            {"messages": [{"role": "user", "content": processed_transcript}]}
    )

    st.markdown(result["messages"][-1].content[-1]["text"])

st.markdown("----")

if file:
    transcript = st.session_state['elevenlabs'].speech_to_text.convert(
        file=file,
        model_id="scribe_v2",  # Model to use
        tag_audio_events=True,  # Tag audio events like laughter, applause, etc.
        language_code="eng",  # Language of the audio file. If set to None, the model will detect the language automatically.
        diarize=True,  # Whether to annotate who is speaking
    )

    pprint(transcript.words, indent=2)

    processed_transcript = ""
    for w in range(len(transcript.words)):
        word = transcript.words[w]
        scribed = f"(Word {w}: {word.text}, Speaker: {word.speaker_id})"
        processed_transcript += scribed 
    pprint(processed_transcript)

    st.markdown(transcript.text)
    st.markdown(processed_transcript)
    result = st.session_state["lai"].invoke(
            {"messages": [{"role": "user", "content": processed_transcript}]}
    )

    st.markdown(result["messages"][-1].content[-1]["text"])
