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
    if provider == "ollama":
        chat_model = init_chat_model(
            f"{provider}:{model}", temperature=0.2
        )
    else:
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

    1. **Phase 1: Comprehensive Transcript Analysis:** Read the provided text transcript. You must fact-check **every single sentence** within the transcript. Do not filter for "important" facts; treat every statement as a claim requiring verification. Extract the **exact quotes** for every sentence.
    2. **Phase 2: Research:** Use `tavily_search` to find evidence for each sentence. Prioritize trusted sources: `.gov`, `.edu`, primary legal documents, peer-reviewed journals, and non-partisan news organizations.
    3. **Phase 3: Deep Verification:** Use `tavily_extract` on the most relevant URLs to gather specific data, context, and publication details for citations. Make sure to verify the url is real and responsive using `check_url`.
    4. **Phase 4: Synthesis:** Compare each sentence to the evidence.
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
