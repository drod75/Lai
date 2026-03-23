---
layout: documentation
title: "Utils Page"
---

This is the utils src code sub page!

<br>

<div class="header-sky-block">
    <div class="header-sky">
        agent_call.py
    </div>
</div>

<br>

tbd

<br>

```python
import streamlit as st
from ratelimit import limits

MINUTE = 60


@limits(calls=5, period=MINUTE)
def call(transcript):
    """The function `call` limits the number of calls to 5 per minute and processes a transcript to
    generate a response.

    Parameters
    ----------
    transcript
        The `transcript` parameter in the `call` function is expected to be a string representing the
    user's input or conversation transcript that will be passed to the agent for processing.

    Returns
    -------
        the text content of the last message in the response messages.

    """
    response = st.session_state["agent"].invoke(
        {"messages": [{"role": "user", "content": transcript}]}
    )

    return response["messages"][-1].content[-1]["text"]
```

<br>

<div class="header-sky-block">
    <div class="header-sky">
        caches.py
    </div>
</div>

<br>

tbd

<br>

```python
from src.agent.agent import agent_pipeline
from elevenlabs.client import ElevenLabs
import streamlit as st


@st.cache_resource
def get_elevenlabs_client():
    """The function `get_elevenlabs_client` returns an instance of the ElevenLabs client using the API key
    stored in the secrets.

    Returns
    -------
        An instance of the ElevenLabs client with the API key retrieved from the secrets file.

    """
    return ElevenLabs(api_key=st.secrets["ELEVENLABS_API_KEY"])


@st.cache_resource
def get_ai_agent():
    """The function `get_ai_agent` returns an AI agent created using a specified provider and model.

    Returns
    -------
        The `get_ai_agent` function is returning an AI agent created using the `agent_pipeline` function
    with the provider and model specified in the secrets file.

    """
    return agent_pipeline(provider=st.secrets["PROVIDER"], model=st.secrets["MODEL"])

```

<br>

<div class="sub-header">
    <div class="sub-header-block">
        ElevenLabs Caching
    </div>
</div>

<br>

tbd

<br>

```python
@st.cache_resource
def get_elevenlabs_client():
    """The function `get_elevenlabs_client` returns an instance of the ElevenLabs client using the API key
    stored in the secrets.

    Returns
    -------
        An instance of the ElevenLabs client with the API key retrieved from the secrets file.

    """
    return ElevenLabs(api_key=st.secrets["ELEVENLABS_API_KEY"])
```

<br>

<div class="sub-header">
    <div class="sub-header-block">
        AI Agent Caching
    </div>
</div>

<br>

tbd

<br>

```python
@st.cache_resource
def get_ai_agent():
    """The function `get_ai_agent` returns an AI agent created using a specified provider and model.

    Returns
    -------
        The `get_ai_agent` function is returning an AI agent created using the `agent_pipeline` function
    with the provider and model specified in the secrets file.

    """
    return agent_pipeline(provider=st.secrets["PROVIDER"], model=st.secrets["MODEL"])

```

<br>

<div class="header-fuchsia-block">
    <div class="header-fuchsia">
        stt.py
    </div>
</div>

<br>

tbd

<br>

```python
import streamlit as st


def speech_to_text(audio):
    """The function `speech_to_text` takes an audio file as input and uses a specified model to transcribe
    the speech in the file, with options to tag audio events, specify language, and annotate speakers.

    Parameters
    ----------
    audio
        The `audio` parameter in the `speech_to_text` function is the input audio file that you want to
    convert to text. This file contains the speech that you want to transcribe into text.

    Returns
    -------
        The function `speech_to_text` returns the transcription of the audio file provided as input, with
    additional annotations such as tagging audio events like laughter, applause, etc., and diarization
    to annotate who is speaking in the audio.

    """
    transcription = st.session_state[
        "elevenlabs"
    ].speech_to_text.convert(
        file=audio,
        model_id="scribe_v2",  # Model to use
        tag_audio_events=True,  # Tag audio events like laughter, applause, etc.
        language_code="eng",  # Language of the audio file. If set to None, the model will detect the language automatically.
        diarize=True,  # Whether to annotate who is speaking
    )

    return transcription.text

```

<br>

<div class="header-fuchsia-block">
    <div class="header-fuchsia">
        text_utilities.py
    </div>
</div>

<br>
    
tbd

<br>

```python
from pypdf import PdfReader


def extract_text(file) -> str:
    """The function `extract_text` reads text from a PDF file using the PdfReader library and returns the
    concatenated text from all pages.

    Parameters
    ----------
    file
        The `extract_text` function takes a file path as input and reads the text content from a PDF file
    located at that path. It uses the `PdfReader` class to read the PDF file and extract text from each
    page. The function then concatenates all the extracted text from each page into a

    Returns
    -------
        The function `extract_text` returns a string containing the extracted text from all pages of the
    PDF file specified as the input parameter.

    """
    reader = PdfReader(file)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text()
    return full_text


def optimizer(text: str) -> str:
    """The `optimizer` function in Python takes a string as input, removes any newline characters, and
    returns the optimized string with leading and trailing whitespaces removed.

    Parameters
    ----------
    text : str
        The `optimizer` function takes a string `text` as input, replaces any newline characters with
    spaces, removes any leading or trailing whitespace, and then returns the optimized text.

    Returns
    -------
        The `optimizer` function takes a string as input, replaces any newline characters with spaces,
    removes any leading or trailing whitespace, and then returns the modified string.

    """
    text = text.replace("\n", " ")
    text = text.strip()
    return text

```

<br>

<div class="sub-header">
    <div class="sub-header-block">
        Extract Text Utility
    </div>
</div>

<br>

tbd

<br>

```python
def extract_text(file) -> str:
    """The function `extract_text` reads text from a PDF file using the PdfReader library and returns the
    concatenated text from all pages.

    Parameters
    ----------
    file
        The `extract_text` function takes a file path as input and reads the text content from a PDF file
    located at that path. It uses the `PdfReader` class to read the PDF file and extract text from each
    page. The function then concatenates all the extracted text from each page into a

    Returns
    -------
        The function `extract_text` returns a string containing the extracted text from all pages of the
    PDF file specified as the input parameter.

    """
    reader = PdfReader(file)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text()
    return full_text
```

<br>

<div class="sub-header">
    <div class="sub-header-block">
        Optimizer Utility
    </div>
</div>

<br>

tbd

<br>

```python
def optimizer(text: str) -> str:
    """The `optimizer` function in Python takes a string as input, removes any newline characters, and
    returns the optimized string with leading and trailing whitespaces removed.

    Parameters
    ----------
    text : str
        The `optimizer` function takes a string `text` as input, replaces any newline characters with
    spaces, removes any leading or trailing whitespace, and then returns the optimized text.

    Returns
    -------
        The `optimizer` function takes a string as input, replaces any newline characters with spaces,
    removes any leading or trailing whitespace, and then returns the modified string.

    """
    text = text.replace("\n", " ")
    text = text.strip()
    return text

```

<br>
