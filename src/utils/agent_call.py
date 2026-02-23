import streamlit as st
from src.agent.agent import agent_pipeline
from ratelimit import limits

MINUTE = 60


@limits(calls=5, period=MINUTE)
def call(transcript):
    response = st.session_state["agent"].invoke(
        {"messages": [{"role": "user", "content": transcript}]}
    )

    return response["messages"][-1].content[-1]["text"]
