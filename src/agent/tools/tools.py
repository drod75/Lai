from langchain_tavily import TavilySearch, TavilyExtract
import streamlit as st


def create_tavily_tools():
    """The function `create_tavily_tools` returns a list of TavilySearch and TavilyExtract objects with
    specific configurations.

    Returns
    -------
        The function `create_tavily_tools()` is returning a list of Tavily tools. The list contains two
    instances: one of `TavilySearch` with specified parameters and one of `TavilyExtract` with specified
    parameters.

    """

    return [
        TavilySearch(
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
        ),
        TavilyExtract(
            extract_depth="basic",
            include_images=False,
        ),
    ]


@st.cache_resource
def give_tools():
    tavily_tools = create_tavily_tools()

    return tavily_tools
