"""
# Audio Test 3
This audio test is centered around testing different speakers and how eleven labs transcribes them.

## Goal
Successfully identify multiple speakers

## Post Test
Work on how to approach multiple speakers, and then work on agent application.
"""

import streamlit as st
from testing.utils.setup import presets
from pprint import pprint
from src.utils.stt import speech_to_text
from src.agent.agent import agent_pipeline

presets()
st.session_state["lai"] = agent_pipeline(
    provider="Google", model_type="gemini-2.5-flash"
)

st.markdown("# Audio Test 2")

c1, c2 = st.columns(2)

with c1:
    st.markdown("## Audio recording")

    audio_recording = st.audio_input("Recoding a line!")
with c2:
    st.markdown("## Audio Input")

    audio_upload = st.file_uploader("Choose an audio file!", type=["wav", "mp3", "m4a"])

with st.expander("Audio Lie Analysis"):
    if audio_recording:
        r_transcript = speech_to_text(audio_recording)
        pprint(r_transcript, indent=2)
        r_result = st.session_state["lai"].invoke(
            {"messages": [{"role": "user", "content": r_transcript}]}
        )

        st.markdown("### Live Audio Result")
        st.markdown(r_result["messages"][-1].content[-1]["text"])
    if audio_upload:
        u_transcript = speech_to_text(audio_upload)
        pprint(u_transcript, indent=2)
        u_result = st.session_state["lai"].invoke(
            {"messages": [{"role": "user", "content": u_transcript}]}
        )

        st.markdown("### Uploaded Audio Result")
        st.markdown(u_result["messages"][-1].content[-1]["text"])

    st.warning("No audio to analyze!")
