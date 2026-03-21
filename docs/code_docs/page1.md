---
layout: documentation
title: "Agent Page"
---

This is the Agent Source CodesSub page, the main structure of the agent folder is as follows:

<br>

<!-- Tree Structure found at https://preline.co/docs/tree-view.html -->
<div class="bg-gray-100 p-4 rounded-lg shadow-sm">
  <div class="hs-accordion-treeview-root" role="tree" aria-orientation="vertical">
    <div class="hs-accordion-group" role="group" data-hs-accordion-always-open>
      <div class="hs-accordion active" role="treeitem" aria-expanded="true" id="agent-root">
        <div class="hs-accordion-heading py-0.5 flex items-center gap-x-0.5 w-full">
          <button class="hs-accordion-toggle size-6 flex justify-center items-center hover:bg-gray-200 rounded-md focus:outline-hidden" aria-expanded="true" aria-controls="agent-root-collapse">
            <svg class="size-4 text-gray-800" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M5 12h14"/></svg>
          </button>
          <div class="grow hs-accordion-selectable px-1.5 rounded-md cursor-pointer">
            <div class="flex items-center gap-x-3">
              <svg class="shrink-0 size-4 text-gray-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"/></svg>
              <div class="grow">
                <span class="text-sm font-medium text-gray-800">agent</span>
              </div>
            </div>
          </div>
        </div>
        <div id="agent-root-collapse" class="hs-accordion-content w-full overflow-hidden transition-[height] duration-300" role="group">
          <div class="hs-accordion-group ps-7 relative before:absolute before:top-0 before:start-3 before:-ms-px before:h-full before:border-s before:border-gray-300" role="group" data-hs-accordion-always-open>
            <div class="hs-accordion active" role="treeitem" aria-expanded="true" id="tools-folder">
              <div class="hs-accordion-heading py-0.5 flex items-center gap-x-0.5 w-full">
                <button class="hs-accordion-toggle size-6 flex justify-center items-center hover:bg-gray-200 rounded-md" aria-expanded="true" aria-controls="tools-folder-collapse">
                  <svg class="size-4 text-gray-800" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M5 12h14"/> </svg>
                </button>
                <div class="grow hs-accordion-selectable px-1.5 rounded-md cursor-pointer">
                  <div class="flex items-center gap-x-3">
                    <svg class="shrink-0 size-4 text-gray-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"/></svg>
                    <div class="grow">
                      <span class="text-sm font-medium text-gray-800">tools</span>
                    </div>
                  </div>
                </div>
              </div>
              <div id="tools-folder-collapse" class="hs-accordion-content w-full overflow-hidden transition-[height] duration-300" role="group">
                <div class="ms-3 ps-3 relative before:absolute before:top-0 before:start-0 before:-ms-px before:h-full before:border-s before:border-gray-300">
                  <div class="hs-accordion-selectable px-2 py-1 rounded-md cursor-pointer" role="treeitem">
                    <div class="flex items-center gap-x-3">
                      <svg class="shrink-0 size-4 text-gray-400" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/></svg>
                      <span class="text-sm text-gray-700">tools.py</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="hs-accordion-selectable px-2 py-1 rounded-md cursor-pointer" role="treeitem">
              <div class="flex items-center gap-x-3">
                <svg class="shrink-0 size-4 text-gray-400" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/></svg>
                <span class="text-sm text-gray-700">agent.py</span>
              </div>
            </div>
          </div>
        </div>
        </div>
      </div>
  </div>
</div>

<br>

Within our Agent Code we have two main pieces, our `agent.py` file which contains the code that builds the agent, and the `/tools/` folder which contains the code the tools our agent uses. Within `/tools/` we have `tools.py` which creates out `check_url` tool, and our `create_tools` function which creates the tools list for our agent. Below will be each section that explains the code, in order of folder structure and file name, starting with `/tools/` and then `agent.py`.

<br>

<div class="p-4 border-l-8 border-sky-600 bg-sky-100 rounded-lg shadow-lg">
    <div class="text-3xl font-bold uppercase text-blue-900 mb-6">
        Tools Folder
    </div>
</div>

<br>

The tools folder contains only one two files, one being the standard `__init__.py` file, and the other being `tools.py` which contains the code for our tools, in this case we only have one tool which is the `check_url` tool, and the function that creates the tools list for our agent which is `create_tools()`. The code for `tools.py` is as follows:

<br>


```python
from langchain_tavily import TavilySearch, TavilyExtract
from langchain.tools import tool
import requests


@tool
def check_url(url: str) -> bool:
    """The `check_url` function in Python uses a HEAD request to efficiently check if a URL is valid by
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

    """
    try:
        # Using stream=True or a HEAD request is more efficient
        response = requests.head(url, allow_redirects=True, timeout=5)
        # Returns True if status code is between 200 and 399
        return response.status_code < 400
    except requests.RequestException:
        return False


def create_tools():
    """The function `create_tools` returns a list of tools for searching, extracting information, and
    checking URLs.

    Returns
    -------
        The `create_tools` function returns a list of tools, including `TavilySearch` with specified
    parameters, `TavilyExtract` with specified parameters, and `check_url`.

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
        check_url,
    ]

```

<br>

Our `check_url` tool checks a URL and returns a boolean value based on if it exists or not, we use a request head and if the status code is between 200 and 399 then we return true, if there is an exception such as a timeout or invalid url, then we return false. The `create_tools` function creates a list of tools for our agent, in this case it creates a `TavilySearch` tool with specific parameters, a `TavilyExtract` tool with specific parameters, and our custom `check_url` tool. This list is returned and used in our `agent.py` file to create the agent with these tools.

<br>

<div class="p-4 border-l-8 border-sky-600 bg-sky-100 rounded-lg shadow-lg">
    <div class="text-3xl font-bold uppercase text-blue-900 mb-6">
        Agent.py
    </div>
</div>

<br>

The `agent.py` file contains the code that creates our agent, it contains the functions, `create_model` which makes our chat model, `create_prompt` which creates the prompt for the agent, and finally `agent_pipeline` which creates the agent pipeline using the previous two functions and the tools created in `tools.py`. The code for `agent.py` is as follows:

<br>

```python
import streamlit as st
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from src.agent.tools.tools import create_tools


def create_model(provider: str, model: str):
    """The function `create_model` initializes a chat model using a specified provider and model with
    specific parameters.

    Parameters
    ----------
    provider : str
        The `provider` parameter refers to the source or company that provides the chat model, such as
    "Google" or "OpenAI".
    model : str
        The `model` parameter in the `create_model` function refers to the specific model that will be used
    for chat generation. It is a string that represents the name or identifier of the model to be
    initialized.

    Returns
    -------
        The function `create_model` returns a chat model initialized with the specified provider and model,
    using the provided API key and temperature setting.

    """
    chat_model = init_chat_model(
        f"{provider}:{model}", api_key=st.secrets["MODEL_API_KEY"], temperature=0.2
    )
    return chat_model


def create_prompt() -> str:
    """The `create_prompt` function generates a detailed system prompt for the core intelligence, Lai, in a
    fact-checking project, outlining its identity, tools, operational instructions, boundaries, output
    format, and research guidelines.

    Returns
    -------
        The `create_prompt()` function returns a detailed system prompt for the LAI (Project Fact-Check)
    system. This prompt includes information about the identity and role of the user as Lai, the tools
    available for use, operational instructions divided into phases, boundaries and constraints to
    follow, output format requirements, and the importance of citations in the response. The prompt
    provides a structured guide for fact-checking

    """
    system_prompt = """
    # System Prompt: LAI (Project Fact-Check)

    ## **Identity & Role**

    You are **Lai**, the core intelligence of the fact-checking project. Your identity is that of a **Fact Checker**: a rigorous, neutral, and highly analytical specialist. Your purpose is to provide objective truth for high-stakes debate audiences by auditing **every sentence** of a provided audio transcript for factual accuracy. As Lai, you do not take sides; you provide evidence-based verdicts with extreme attention to nuance.

    ## **Tools**

    Lai has a total of three tools available for use, in order they are:
    1. `tavily_search`: This tool allows Lai to execute a search query using Tavily Search.
    2. `tavily_extract`: This tool allows Lai to extract web page content from one or more specified URLs using Tavily Extract.
    3. `check_url`: takes in a website url and checks the response code to see if the url works.

    ## **Operational Instructions**

    4. **Phase 1: Comprehensive Transcript Analysis:** Read the provided text transcript. You must fact-check **every single sentence** within the transcript. Do not filter for "important" facts; treat every statement as a claim requiring verification. Extract the **exact quotes** for every sentence.
    5. **Phase 2: Research:** Use `tavily_search` to find evidence for each sentence. Prioritize trusted sources: `.gov`, `.edu`, primary legal documents, peer-reviewed journals, and non-partisan news organizations.
    6. **Phase 3: Deep Verification:** Use `tavily_extract` on the most relevant URLs to gather specific data, context, and publication details for citations. Make sure to verify the url is real and responsive using `check_url`.
    7. **Phase 4: Synthesis:** Compare each sentence to the evidence.
    * **True:** The sentence is fully supported by credible evidence.
    * **False:** The sentence is contradicted by credible evidence.
    * **Nuanced:** The sentence is partially true but lacks context or is presented in a misleading way.
    * **Unverified:** No credible evidence could be found to prove or disprove the statement (e.g., a purely personal anecdote or a claim with no public record).



    ## **Boundaries & Constraints**

    * **Source Control:** Explicitly **ignore** blogs, opinion pieces, social media threads (e.g., X, Reddit), and known conspiracy websites.
    * **Exhaustive Scope:** You must not skip sentences. Even if a sentence seems trivial, verify its accuracy. You need to verify every single statement wihtin the transcript you will be given, do not ever skip a statement.
    * **Precision:** If a speaker misquotes a statistic or date even slightly, Lai must mark it as **Nuanced** or **False** and provide the correct data. If a user also states something that contains clear evidence it is wrong, Lai must mark their statement as False.
    * **Citations:** All citations must be made using the same url's that were obtained using the `tavily_search` tool.
    * **Reasearch:** All research should be made using `tavily_extract` on sites that have valid url's, and have been obtained using `tavily_search`
    * **URLS**: ALl urls that you extract from, should be verified and obtained soley from `tavily_search`
    * **Format**: There must be an equal amount results to facts.

    ## **Output Format**

    You must structure your response exactly as follows:

    ### 🎙️ Fact Section

    * **Fact 1:** "[Exact Quote of Sentence 1]"
    * **Fact 2:** "[Exact Quote of Sentence 2]"
    *(Continue for all sentences in the transcript)*

    ### ⚖️ Result Section

    * **Result [Number]:**
    (Intentional tab below for items under result [Number], ignore this line)
        * **Status:** [True / False / Unverified / Nuanced]
        * **Analysis:** [A concise, professional explanation of the evidence provided by Lai regarding this specific sentence.]
        * **Citations (MLA):** Author's Last Name, First Name. "Title of Article." *Website Name*, Day Month Year, URL.
    * **Result [Number]:**
    (Intentional tab below for items under result [Number], ignore this line)
        * **Status:** [True / False / Unverified / Nuanced]
        * **Analysis:** [A concise, professional explanation of the evidence provided by Lai regarding this specific sentence.]
        * **Citations (MLA):** Author's Last Name, First Name. "Title of Article." *Website Name*, Day Month Year, URL.
    * (Continue)



    ### Final Step

    Remember, the "MLA" citation is a crucial piece of evidence for the debaters using **Lai**. If Lai cannot find a specific author for a source, it should start the citation with the **"Article Title"** instead. Every link should be valid, and not lead to an empty site, or a site that does not exist.

     """

    return system_prompt


def agent_pipeline(provider: str, model: str):
    """The function `agent_pipeline` creates an agent with a specified provider and model for chat
    interactions.

    Parameters
    ----------
    provider : str
        The `provider` parameter in the `agent_pipeline` function likely refers to the service provider or
    platform that will be used for creating the chatbot model. This could be a specific company or
    service that offers tools and resources for building chatbots.
    model : str
        The `model` parameter in the `agent_pipeline` function refers to the specific model that will be
    used by the agent for its chat functionality. This model could be a machine learning model, a
    rule-based model, or any other type of model that the agent will utilize to interact with users.

    Returns
    -------
        An agent object is being returned from the agent_pipeline function.

    """
    chat_model = create_model(provider, model)
    system_prompt = create_prompt()
    tools = create_tools()
    agent = create_agent(model=chat_model, tools=tools, system_prompt=system_prompt)

    return agent

```

<br>

Our `create_model` function initializes a chat model using the specified provider and model, along with an API key and temperature setting. The `create_prompt` function generates a detailed system prompt for our agent, Lai, outlining its identity, tools, operational instructions, boundaries, output format, and research guidelines. Finally, the `agent_pipeline` function creates an agent using the chat model, tools, and system prompt created by the previous functions. This agent can then be used to perform fact-checking tasks as outlined in the system prompt.
