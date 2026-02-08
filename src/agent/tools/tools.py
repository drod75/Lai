from langchain.tools import tool
from langchain_tavily import TavilySearch, TavilyExtract
import streamlit as st


@tool
def speech_to_text(audio):
    transcription = st.session_state["elevenlabs"].speech_to_text.convert(
        file=audio,
        model_id="scribe_v2",  # Model to use
        tag_audio_events=True,  # Tag audio events like laughter, applause, etc.
        language_code="eng",  # Language of the audio file. If set to None, the model will detect the language automatically.
        diarize=True,  # Whether to annotate who is speaking
    )

    return transcription


def create_tavily_tools():
    search = TavilySearch(
        max_results=5,
        topic="general",
        # include_answer=False,
        # include_raw_content=False,
        # include_images=False,
        # include_image_descriptions=False,
        search_depth="advanced",
        # time_range="day",
        # include_domains=None,
        # exclude_domains=None
    )

    extract = TavilyExtract(
        extract_depth="basic",
        include_images=False,
    )

    return [search, extract]


@st.cache_resource
def give_tools():
    tavily_tools = create_tavily_tools()
    tavily_tools.extend(speech_to_text)

    return tavily_tools
