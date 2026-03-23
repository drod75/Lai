import streamlit as st
from src.utils.stt import speech_to_text
from src.utils.text_utilities import optimizer, extract_text
from src.utils.agent_call import call
from src.utils.caches import get_ai_agent, get_elevenlabs_client


if "last_entry" not in st.session_state:
    st.session_state["last_entry"] = None
if "last_response" not in st.session_state:
    st.session_state["last_response"] = None

st.session_state["elevenlabs"] = get_elevenlabs_client()
st.session_state["agent"] = get_ai_agent()

st.markdown("# :violet[Lai 🤖]", text_alignment="center")
st.markdown(
    ":violet[*__To create a world where people on an influential platform can not lie to the world__*]",
    text_alignment="center",
)

with st.expander(":blue[Audio Input]", icon=":material/speaker:"):
    c1, c2 = st.columns(2, border=True)

    with c1:
        st.header("Recording Option")
        audio_record = st.audio_input("Record your conversation here!")
        if audio_record:
            st.session_state["last_entry"] = optimizer(speech_to_text(audio_record))
            st.session_state["last_response"] = None

    with c2:
        st.header("Audio File Option")
        audio_file = st.file_uploader(
            "Choose an audio file to input!", type=["wav", "mp3", "m4a"]
        )
        if audio_file:
            st.session_state["last_entry"] = optimizer(speech_to_text(audio_file))
            st.session_state["last_response"] = None

with st.expander(":blue[File Input]", icon=":material/upload_file:"):
    c1, c2 = st.columns(2, border=True)

    with c1:
        st.header("PDF File Option")
        pdf = st.file_uploader("Choose a PDF to input!", type=["pdf"])
        if pdf:
            st.session_state["last_entry"] = optimizer(extract_text(pdf))
            st.session_state["last_response"] = None

    with c2:
        st.header("Text based File Option")
        text_file = st.file_uploader(
            "Choose a Text based file to input!", type=["txt", "html"]
        )
        if text_file:
            dedoded_file = text_file.getvalue().decode("utf-8")  # type: ignore
            st.session_state["last_entry"] = optimizer(dedoded_file)
            st.session_state["last_response"] = None


with st.expander(":blue[Raw Input]", icon=":material/text_fields:"):
    st.header("Text Option")
    text_input = st.text_input("Transcript goes here!", key="text_in")
    if text_input and text_input != st.session_state["last_entry"]:
        st.session_state["last_entry"] = optimizer(text_input)
        st.session_state["last_response"] = None


if st.session_state["last_entry"] and not st.session_state["last_response"]:
    with st.spinner("Awaiting response..."):
        st.session_state["last_response"] = call(st.session_state["last_entry"])

with st.container(border=True):
    st.markdown("## :violet[AI Fact Check]", text_alignment="center")
    if st.session_state["last_response"]:
        st.markdown(st.session_state["last_response"])
    else:
        st.info("No current response available, please try on of the options above!")
