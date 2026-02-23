import streamlit as st
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from typing import Literal
from src.agent.tools.tools import give_tools


@st.cache_resource
def create_model(
    provider: Literal["Google", "Ollama"],
    model_type: Literal[
        "llama3.2:1b", "llama3.2:3b", "gemini-3-flash", "gemini-2.5-flash"
    ],
):
    """The function `create_model` creates a chatbot model based on the specified provider and model type.

    Parameters
    ----------
    provider : Literal["Google", "Ollama"]
        The `provider` parameter specifies the provider of the chatbot model, which can be either "Google"
    or "Ollama".
    model_type : Literal["llama3.2:1b", "llama3.2:3b", "gemma3:4b", "gemini-3-flash", "gemini-2.5-flash"]
        The `model_type` parameter specifies the type of model to be created. The available options are:

    Returns
    -------
        The `create_model` function returns an instance of either `ChatGoogleGenerativeAI` or `ChatOllama`
    based on the specified `provider` and `model_type` parameters.

    """
    if provider == "Google":
        model = ChatGoogleGenerativeAI(model=model_type)
        return model
    else:
        model = ChatOllama(model=model_type, temperature=0.4)
        return model


@st.cache_resource
def create_prompt():
    system_prompt = """
    # System Prompt: LAI (Project Fact-Check)

    ## **Identity & Role**

    You are **Lai**, the core intelligence of the fact-checking project. Your identity is that of a **Debate Arbiter**: a rigorous, neutral, and highly analytical specialist. Your purpose is to provide objective truth for high-stakes debate audiences by auditing **every sentence** of a provided audio transcript for factual accuracy. As Lai, you do not take sides; you provide evidence-based verdicts with extreme attention to nuance.

    ## **Operational Instructions**

    1. **Phase 1: Comprehensive Transcript Analysis:** Read the provided text transcript. You must fact-check **every single sentence** within the transcript. Do not filter for "important" facts; treat every statement as a claim requiring verification. Extract the **exact quotes** for every sentence.
    2. **Phase 2: Research:** Use `tavily_search` to find evidence for each sentence. Prioritize trusted sources: `.gov`, `.edu`, primary legal documents, peer-reviewed journals, and non-partisan news organizations.
    3. **Phase 3: Deep Verification:** Use `tavily_extract` on the most relevant URLs to gather specific data, context, and publication details for citations.
    4. **Phase 4: Synthesis:** Compare each sentence to the evidence.
    * **True:** The sentence is fully supported by credible evidence.
    * **False:** The sentence is contradicted by credible evidence.
    * **Nuanced:** The sentence is partially true but lacks context or is presented in a misleading way.
    * **Unverified:** No credible evidence could be found to prove or disprove the statement (e.g., a purely personal anecdote or a claim with no public record).



    ## **Boundaries & Constraints**

    * **Source Control:** Explicitly **ignore** blogs, opinion pieces, social media threads (e.g., X, Reddit), and known conspiracy websites.
    * **Exhaustive Scope:** You must not skip sentences. Even if a sentence seems trivial, verify its accuracy. You need to verify every single statement wihtin the transcript you will be given, do not ever skip a statement.
    * **Precision:** If a speaker misquotes a statistic or date even slightly, Lai must mark it as **Nuanced** or **False** and provide the correct data.

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

    Remember, the "MLA" citation is a crucial piece of evidence for the debaters using **Lai**. If Lai cannot find a specific author for a source, it should start the citation with the **"Article Title"** instead.

     """

    return system_prompt


@st.cache_resource
def agent_pipeline(
    provider: Literal["Google", "Ollama"],
    model_type: Literal[
        "llama3.2:1b", "llama3.2:3b", "", "gemini-3-flash", "gemini-2.5-flash"
    ],
):
    """The function `agent_pipeline` creates an agent with a specified provider and model type.

    Parameters
    ----------
    provider : Literal["Google", "Ollama"]
        The `provider` parameter specifies the provider of the agent model. It can be either "Google" or
    "Ollama".
    model_type : Literal["llama3.2:1b", "llama3.2:3b", "gemini-3-flash"]
        The `model_type` parameter specifies the type of model to be used in the agent pipeline. The
    available options are:

    Returns
    -------
        The `agent_pipeline` function is returning an agent object that is created using the specified
    provider and model type. The agent is created by calling the `create_model`, `create_prompt`,
    `give_tools`, and `create_agent` functions with the appropriate parameters.

    """
    model = create_model(provider, model_type)  # type: ignore
    system_prompt = create_prompt()
    tools = give_tools()
    agent = create_agent(model=model, tools=tools, system_prompt=system_prompt)

    st.session_state["agent"] = agent
