from langchain_tavily import TavilySearch, TavilyExtract
from langchain.tools import tool
import streamlit as st
import requests

@tool
def check_url(url: str) -> bool:
    '''The `check_url` function in Python uses a HEAD request to efficiently check if a URL is valid by
    verifying the status code falls within the range of 200 to 399.
    
    Parameters
    ----------
    url : str
        The `url` parameter is a string that represents the URL of a website or resource that you want to
    check for validity.
    
    Returns
    -------
        The function `check_url` returns a boolean value. It returns `True` if the status code of the
    response from the provided URL is between 200 and 399, indicating a successful request. If there is
    an exception during the request (e.g., network issue, invalid URL), it returns `False`.
    
    '''
    try:
        # Using stream=True or a HEAD request is more efficient
        response = requests.head(url, allow_redirects=True, timeout=5)
        # Returns True if status code is between 200 and 399
        return response.status_code < 400
    except requests.RequestException:
        return False 


def create_tools():
    '''The function `create_tools` returns a list of tools for searching, extracting information, and
    checking URLs.
    
    Returns
    -------
        The `create_tools` function returns a list of tools, including `TavilySearch` with specified
    parameters, `TavilyExtract` with specified parameters, and `check_url`.
    
    '''
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
        check_url
    ]
