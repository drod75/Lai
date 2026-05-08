import streamlit as st
from src.utils.stt import speech_to_text
from src.utils.text_utilities import optimizer, extract_text
from src.utils.agent_call import call
from src.utils.caches import get_ai_agent, get_elevenlabs_client

if "last_entry" not in st.session_state:
    st.session_state["last_entry"] = None
if "last_response" not in st.session_state:
    st.session_state["last_response"] = None

try:
    st.session_state["elevenlabs"] = get_elevenlabs_client()
except Exception as e:
    st.session_state["logger"].error(
        f"**Error**: Failed to establish ElevenLabs Client!\n{e}"
    )

try:
    st.session_state["agent"] = get_ai_agent()
except Exception as e:
    st.session_state["logger"].error(
        f"**Error**: Failed to establish Lai AI-Agent!\n{e}"
    )

st.markdown("# :violet[Lai 🤖]", text_alignment="center")
st.markdown(
    ":violet[*__To create a world where people on an influential platform can not lie to the world__*]",
    text_alignment="center",
)

with st.expander(":violet[Details]", icon=":material/details:"):
    st.markdown("""
        Welcome to ***Lai***, the purpose of ***Lai*** is to fact check pieces of conversations, from recorded audio to text transcriptions, ***Lai*** can fact check those pieces of text.
        There are three options tha are available...
        1. **Audio:** This allows you to input audio files, or record audio directly to be transcribed.
        2. **File:** This allows you to input a PDF, or a text based file such as a txt or html file.
        3. **Raw:** This allows you to just type in text, such as pasting the transcript.
        """)

with st.expander(":violet[Audio Input]", icon=":material/speaker:"):
    c1, c2 = st.columns(2, border=True)

    with c1:
        st.header("Recording Option")
        audio_record = st.audio_input("Record your conversation here!")
        if audio_record:
            temp = None
            try:
                temp = speech_to_text(audio_record)
            except Exception as e:
                st.session_state["logger"].error(
                    f"**Error**: Failed to invoke Eleven Labs to transcribe text!\n{e}"
                )

            try:
                st.session_state["last_entry"] = optimizer(temp)
            except Exception as e:
                st.session_state["logger"].error(
                    f"**Error**: Failed to optimize text!\n{e}"
                )

            st.session_state["last_response"] = None

    with c2:
        st.header("Audio File Option")
        audio_file = st.file_uploader(
            "Choose an audio file to input!", type=["wav", "mp3", "m4a"]
        )
        if audio_file:
            temp = None
            try:
                temp = speech_to_text(audio_file)
            except Exception as e:
                st.session_state["logger"].error(
                    f"**Error**: Failed to invoke Eleven Labs to transcribe text!\n{e}"
                )

            try:
                st.session_state["last_entry"] = optimizer(temp)
            except Exception as e:
                st.session_state["logger"].error(
                    f"**Error**: Failed to optimize text!\n{e}"
                )

            st.session_state["last_response"] = None

with st.expander(":violet[File Input]", icon=":material/upload_file:"):
    c1, c2 = st.columns(2, border=True)

    with c1:
        st.header("PDF File Option")
        pdf = st.file_uploader("Choose a PDF to input!", type=["pdf"])
        if pdf:
            temp = None
            try:
                temp = extract_text(pdf)
            except Exception as e:
                st.session_state["logger"].error(
                    f"**Error**: Failed to extract text from PDF!\n{e}"
                )

            try:
                st.session_state["last_entry"] = optimizer(temp)
            except Exception as e:
                st.session_state["logger"].error(
                    f"**Error**: Failed to optimize text!\n{e}"
                )

            st.session_state["last_response"] = None

    with c2:
        st.header("Text based File Option")
        text_file = st.file_uploader(
            "Choose a Text based file to input!", type=["txt", "html"]
        )
        if text_file:
            try:
                decoded_file = text_file.getvalue().decode("utf-8")  # type: ignore
                st.session_state["last_entry"] = optimizer(decoded_file)
            except Exception as e:
                st.session_state["logger"].error(
                    f"**Error**: Failed to optimize text!\n{e}"
                )

            st.session_state["last_response"] = None


with st.expander(":violet[Raw Input]", icon=":material/text_fields:"):
    st.header("Text Option")
    text_input = st.text_input("Transcript goes here!", key="text_in")
    if text_input and text_input != st.session_state["last_entry"]:
        try:
            st.session_state["last_entry"] = optimizer(text_input)
        except Exception as e:
            st.session_state["logger"].error(
                f"**Error**: Failed to optimize text!\n{e}"
            )

        st.session_state["last_response"] = None


if st.session_state["last_entry"] and not st.session_state["last_response"]:
    with st.spinner("Awaiting response..."):
        try:
            st.session_state["last_response"] = call(st.session_state["last_entry"])
        except Exception as e:
            st.session_state["logger"].error(
                f"**Error**: Failed to establish response from Lai!\n{e}"
            )

with st.container(border=True):
    st.markdown("## :violet[AI Fact Check]", text_alignment="center")
    if st.session_state["last_response"]:
        st.markdown(st.session_state["last_response"])

        st.download_button(
            label="Download Fact Check",
            data=st.session_state["last_response"],
            file_name="fact_check_results.md",
            mime="text/markdown",
            icon=":material/download:",
        )
    else:
        st.info("No current response available, please try on of the options above!")
