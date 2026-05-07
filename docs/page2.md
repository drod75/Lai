---
layout: analysis
title: "Analysis Page"
---
<div class="header-sky-block">
    <div class="header-sky">
        Introduction
    </div>
</div>

<br>

When watching the news, one thought would always come to mind depending on the channel, *"Why are they leaving out this piece of info?"*, *"Why are they talking about this instead of that?"*, and one thing I had always hoped for was lying to be caught and exposed. In conversations with friends, when it is about something they so confident in and you know it's wrong, would make it funny if they were caught lying. Overall the ability to be able to catch lies and expose them is something that is very satisfying and something that I have always wanted to be able to do. So that is why I choose to make Lai, the AI Lie detector.

<br>

<div class="header-sky-block">
    <div class="header-sky">
        Initial Thoughts
    </div>
</div>

<br>

When first thinking about how I would make Lai, I knew that I needed to create an agent who could analyze a conversation and continuously analyze the conversation, via researching and providing evidence as to why something it true or false. The foundation of this agent would have to be in python, and would have to be able to allow others to use any LLM provider, so that no one person or group has a monopoly on the technology, I also wanted to make it so that the agent could be used in a variety of contexts, such as in a news article, in a conversation, or in a debate, these parameters made me have to think deeply about what the project needs to be built on.

<br>

<div class="sub-header">
    <div class="sub-header-block">
        Initial preparations
    </div>
</div>

<br>

Since I had the main idea and core function of my project thought out, I needed to create a plan for how I would build it, and what I would need to build it. I had heard about some api's and resources that would help my goal but needed to create a game plan on how to approach this project, and how to break it down into achievable goals. My main inspiration for a timeline is below:
<img src="assets/images/timeline.png" alt="Timeline" class="timeline-image">

<br>

This timeline would serve as a rough guide for how I would approach the project, and would help me stay on track and make sure that I was making progress towards my goal. First I knew that I would be using langchain for the agent framework, as it allowed for support for multiple LLM providers. For the audio work, aka the speech to text, I would use Elevenlabs, as it's pricing and uses were more than enough to be able to accommodate my work. For the web tools, after some research I found that the best way to do this would be using Tavily, since it allows for easy web crawling and extraction, along with its langchain integration which would make it easier to setup. After deciding my libraries, I did more research on how they function and operate to be able to understand them more clearer. For the UI I decided to use streamlit, as it is a great tool for building web apps, and would allow me to focus more on the functionality of the agent rather than the design of the UI.

<br>

<div class="header-fuchsia-block">
    <div class="header-fuchsia">
        Technologies Explained
    </div>
</div>

<br>

<div class="sub-header">
    <div class="sub-header-block">
        Python
    </div>
</div>

<br>

Python, is a programming lanuage used by many for a wide variety of topics, from Data Analysis, to Software Engineering, and more Recently LLM usage, Python has a wide variety of uses and has several hundred libraries which can help it do so, as such it was the first choice for my project, as it more closely aligns with my career goals and current skills. 

As per the offical documentation of python, "Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms." ([Python Docs](https://docs.python.org/3/tutorial/index.html), Tutorial). Python is indeed very good at rapidly creating code, because of this, creating libraries from scratch, and having to do grueling hours of work was out of the question, this made it easier to work with.

<br>

<div class="sub-header">
    <div class="sub-header-block">
        Langchain
    </div>
</div>

<br>

LangChain is a platform for agent engineering, it can be used to create powerful agents that are able to do various tasks, and interact with various tools, it is the backbone of Lai, as with it we are able to create an agent that can interact with the internet, via it's tools. One of the most important aspects of this project is the ability for the public and beyond to use it as they please, so as a result, `init_chat_model()` is used so people can drop in and replace the LLM powering Lai with any model they please.

Langchain also comes with the ability to create agents, via the `create_agent()` method, this is used to create a REACT loop, which in turn allows the agent to progess through it's work. This is essential for Lai, as it allows Lai to work on it's task in various steps, think about it's previous step's result's, and work forward from there. 

In the future the project will showcase the ability of using fine tuned models specifically meant for Lai, and that model will also be available to the public, and should work with LangChain just fine.

<br>

<div class="sub-header">
    <div class="sub-header-block">
        Tavily
    </div>
</div>

<br>

Tavily is a tool that allows AI to perform real time web search, this can be done many methods, some of which being crawling and extracting. Crawling allows the AI to go through various web page's and web sub pages, and extracting allows AI to get the information and content of a web page easy.

<br>

<div class="sub-header">
    <div class="sub-header-block">
        ElevenLabs
    </div>
</div>

<br>

Eleven Labs is a product that allows for AI generated audio, as well as speech transcriptions, its use cases are very high, and it provides great service for what it does, Eleven labs allowed Lai to create transcripts for audio, and in a fast and accurate capacity.

<br>

<div class="sub-header">
    <div class="sub-header-block">
        streamlit
    </div>
</div>

<br>

"Streamlit is an open-source app framework that is a breeze to get started with.", [Streamlit Main Page](https://streamlit.io/). Streamlit allows for easy and fast web app development, and due it's python centric nature, it allows for more focus on functionality then spending hours on design. This allowed for Lai to be developed much faster, as an entire backend and frontend did not have to be developed, so the focus can be the agent behind Lai instead.

<br>

<div class="header-violet-block">
    <div class="header-violet">
        Post Project Clarity
    </div>
</div>

After the main project part was done and in a good place, the following work was done to make the project better, via adding more features and functionality. 

<div class="sub-header">
    <div class="sub-header-block">
        Fine Tuning
    </div>
</div>

Towards the end of the project, I wanted to fine tune a model, the reasons being displayed under:
- To have the model be better at it's task.
- To have a model that can be as efficient as high end models, but run on lower hardware.
- Expand the scope of the project.
The model that was fine tuned was `llama-3-8b-Instruct-bnb-4bit`, the reason for this was that it was a smaller model, and that it was already instruction tuned, so it would be easier to fine tune for my specific task. The fine tuning process was done via the `Unsloth` library, and the dataset used was a HuggingFace dataset, to be specific, the dataset was created via a combination of the following HuggingFace dataset:
- `jpd459/resplit_multi_fact_checking_dataset_resampling`

<div class="sub-header">
    <div class="sub-header-block">
        Unfinished and Future Work
    </div>
</div>

The future that Lai holds is bright, several things can be done to 
- Statistics
- More developed analysis
- Results Export
- Speech Analysis
- Real Time Analysis
- Active domain registry to determine if a website is credible or not
- Command Line Interface
- Users + Ranked Lying Leaderboards


