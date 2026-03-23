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
from dotenv import load_dotenv
from src.utils.stt import speech_to_text
from src.utils.text_utilities import optimizer, extract_text
from src.utils.agent_call import call
from src.utils.caches import get_ai_agent, get_elevenlabs_client


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

<br>

<div class="sub-header">
    <div class="sub-header-block">
    </div>
</div>

<br>

The

<br>

```python
```

<br>

<div class="sub-header">
    <div class="sub-header-block">
        File Input
    </div>
</div>

<br>

The

<br>

```python
```

<br>

<div class="sub-header">
    <div class="sub-header-block">
        Raw Input
    </div>
</div>

<br>

The

<br>

```python
```

<br>

<div class="sub-header">
    <div class="sub-header-block">
        Agent Calling and Response
    </div>
</div>

<br>

The

<br>

```python
```

<br>