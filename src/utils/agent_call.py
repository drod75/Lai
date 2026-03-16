import streamlit as st
from ratelimit import limits

MINUTE = 60


@limits(calls=5, period=MINUTE)
def call(transcript):
    '''The function `call` limits the number of calls to 5 per minute and processes a transcript to
    generate a response.
    
    Parameters
    ----------
    transcript
        The `transcript` parameter in the `call` function is expected to be a string representing the
    user's input or conversation transcript that will be passed to the agent for processing.
    
    Returns
    -------
        the text content of the last message in the response messages.
    
    '''
    response = st.session_state["agent"].invoke(
        {"messages": [{"role": "user", "content": transcript}]}
    )

    return response["messages"][-1].content[-1]["text"]
