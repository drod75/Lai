---
layout: documentation
title: "UI Page"
---

This is **UI Source Code Page**, within our `/src/ui` folder, we have only one file, that being `main.py`, this file represents where our main UI code is, and where all the Utilities are being called in.

<br>

<div class="header-sky-block">
    <div class="header-sky">
        Main.py
    </div>
</div>

<br>

The `main.py` File is where our site comes to life, this is where the the UI that the user see's 24/7 appears, it is attempted to be a site where everything comes together, rather than everything being placed in one location. The next few sections will go into depth around parts of the code, and how they work.

<br>

```python
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

```

<br>

<div class="sub-header">
    <div class="sub-header-block">
        Caching and Pre work
    </div>
</div>

<br>

The code below sets up not only some important session state variables, but also our site's main header and tagline, these processes are important to be cached at the start of the site, as they are not only used throughout the site, but also need to be set up before any user interaction, as they are used in the main body of the site.

<br>

```python
if "last_entry" not in st.session_state:
    st.session_state["last_entry"] = None
if "last_response" not in st.session_state:
    st.session_state["last_response"] = None

load_dotenv()


st.session_state["elevenlabs"] = get_elevenlabs_client()
st.session_state["agent"] = get_ai_agent()

st.markdown("# :violet[Lai 🤖]", text_alignment="center")
st.markdown(
    ":violet[*__To create a world where people on an influential platform can not lie to the world__*]",
    text_alignment="center",
)
```

<br>

<div class="sub-header">
    <div class="sub-header-block">
    Audio Input
    </div>
</div>

<br>

The Audio input option contains our `st.expander()` block, which house's both our audio input options, and allows them to be collapsed to make the screen less cluttered. Using `st.columns()` we are able to place our inputs side by side, and we reuse this UI look later on. The first audio option, **_"Recording Option"_**, allows the user to record audio directly into the site, and then uses our `speech_to_text()` utility to transcribe the audio, and then our `optimizer()` utility to optimize the transcript for the agent. The second audio option, **_"Audio File Option"_**, allows the user to upload an audio file, and then uses the same utilities as the first option to transcribe and optimize the transcript.

<br>

```python
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

```

<br>

<div class="sub-header">
    <div class="sub-header-block">
        File Input
    </div>
</div>

<br>

The next input option is our file input option, which again uses an `st.expander()` block to house two different file input options, the first being a **_"PDF File Option"_**, which allows the user to upload a PDF file, and then uses our `extract_text()` utility to extract the text from the PDF, and then optimizes it for the agent. The second option is a **_"Text based File Option"_**, which allows the user to upload a text based file, such as a .txt or .html file, and then decodes the file, and optimizes it for the agent.

<br>

```python
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
```

<br>

<div class="sub-header">
    <div class="sub-header-block">
        Raw Input
    </div>
</div>

<br>
 
The last input option is our raw input option, which allows the user to input text directly into the site, this is useful for quick testing, or for users who already have a transcript or text that they want to test, and don't want to go through the process of uploading a file. Again, we optimize the text for the agent before storing it in session state.

<br>

```python
with st.expander(":blue[Raw Input]", icon=":material/text_fields:"):
    st.header("Text Option")
    text_input = st.text_input("Transcript goes here!", key="text_in")
    if text_input and text_input != st.session_state["last_entry"]:
        st.session_state["last_entry"] = optimizer(text_input)
        st.session_state["last_response"] = None
```

<br>

<div class="sub-header">
    <div class="sub-header-block">
        Agent Calling and Response
    </div>
</div>

<br>

The final part of our site is where we call our agent, and finally display the results, we first call our agent using the `call()` utility from `/src/utils/agent_call.py`, and then we display the response in a container, if there is no response, we display an info message prompting the user to try one of the input options.

<br>

```python
with st.spinner("Awaiting response..."):
    st.session_state["last_response"] = call(st.session_state["last_entry"])

with st.container(border=True):
    st.markdown("## :violet[AI Fact Check]", text_alignment="center")
    if st.session_state["last_response"]:
        st.markdown(st.session_state["last_response"])
    else:
        st.info("No current response available, please try on of the options above!")

```

<br>