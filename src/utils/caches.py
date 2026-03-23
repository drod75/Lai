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
