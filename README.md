<p align="center">
  <img src="docs/assets/logo/Lai.png" alt="Lai-banner" style="width:300px;"/>
</p>

<h1 align="center" id="readme-top">🤖 Lai</h1>

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/drod75/Lai/blob/main/LICENSE)
[![Email](https://img.shields.io/badge/Email-dr507498@gmail.com-blue)](mailto:dr507498@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/david-rodriguez-nyc/)
[![Stars](https://img.shields.io/github/stars/drod75/Lai)](https://github.com/drod75/Lai/stargazers)
[![Watching](https://img.shields.io/github/watchers/drod75/Lai)](https://github.com/drod75/Lai/watchers)
[![Forks](https://img.shields.io/github/forks/drod75/Lai)](https://github.com/drod75/Lai/forks)

<p align="center" style="font-size: 20px; font-weight: bold; font-style: italic;">The AI powered Lie Detector!</p>

<details open>
  <summary>Table of Contents</summary>
  
- [About](#about)
  - [About the Creator](#about-the-creator)
  - [Motivation](#motivation)
  - [Timeline](#timeline)
  - [Future](#future)
- [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Explanation](#explanation)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
- [Extra Information](#extra-information)
- [Contributing](#contributing)
- [License](#license)
</details>

## About

Welcome to Lai, the AI-powered lie detector designed to analyze transcripts and determine if a statement is true or false via web scraping. Lai utilizes an Agent to scrape the web for relevant information, and provide the user with a friendly response formatted in various bullet points, and citations. 

### About the Creator

Below is some information about me, the creator of Lai:

* **Name:** David Rodriguez
* **College:** Brooklyn College
* **Year:** Senior
* **Extracurricular Activities:**
    * Undergraduate Student Government Senator
    * Former CodePath Ambassador
    * Club Treasurer


### Motivation

The motivation behind creating Lai stemmed from a desire to fact check politicians live, in the age of the internet information is abundant, but due to various factors such as bias, and misinformation, it can be difficult to determine the truth. Lai prioritizes providing users with accurate information, and citations to back up its claims, making it a valuable tool for anyone looking to fact check statements in real time. When creating Lai I always wanted to add citations, in order to make sure users could verify the information themselves, and not just trust what the AI says, like we should with people.

### Timeline
Image of the projected project timeline.

<p align="center" style="background-color: white;">
  <img style="background-color: white; width:500px; height:600px;" src="docs/assets/images/timeline.png" alt="timeline">
</p>

### Future

The future of Lai is interesting, while the tools and foundation is built, there are many other paths that can branch off from this project. Future goals are below
- [x] Fine tuning a custom model
- [ ] Statistics
- [ ] More developed analysis
- [ ] Results Export
- [ ] Speech Analysis
- [ ] Real Time Analysis
- [ ] Active domain registry to determine if a website is credible or not
- [ ] Command Line Interface
- [ ] Users + Ranked Lying Leaderboards

## Features

### Technologies Used
The following technologies were utilized to build the Lai assistant:

* **Language**
    - [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

* **AI & Logic**
    - [![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com/)

* **Tools & Voice**
    - [![Tavily](https://img.shields.io/badge/Tavily-FF5733?style=for-the-badge&logo=search&logoColor=white)](https://tavily.com/)
    - [![ElevenLabs](https://img.shields.io/badge/Eleven%20Labs-000000?style=for-the-badge&logo=elevenlabs&logoColor=white)](https://elevenlabs.io/)

* **UI**
    - [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

### Explanation

The foundation of this project is Python, the reason being that it is a versatile language with various libraries that are needed for this project. The main UI is built using Streamlit, this is because of the simple requirements needed for Lai, it is exactly what is needed. The agent is built on LangChain, this is because Langchain not only allows for a wide variety of tools to be used, but for a wide variety of large language models to be used as well, in this case Google Gemini. The main tool used is Tavily, this is because of its ability to scrape the web in real time, and provide the agent with relevant information. Finally, ElevenLabs is used to transcript audio input, and provide the LLM with a text input for analysis.

<p align="right"><a href="#readme-top">Back to top</a></p>

## Getting Started
To get a local copy of the project up and running, follow the instructions below.

### Prerequisites

- Have Python installed on your machine (version 3.8 or higher).
- Obtain API keys for the following services:
  - Google Gemini
  - Tavily
  - ElevenLabs

### Setup

- Install the required dependencies using either Pip or UV(Recommended).
  - Using Pip:
    ```bash
    pip install -r requirements.txt
    ```
  - Using UV:
    ```bash
    uv venv
    uv sync
- Run the application:
    ```bash
    streamlit run main.py
    ```


<p align="right"><a href="#readme-top">Back to top</a></p>

## Extra Information

Lai comes with langchain ollama and gemini, but due to the agent's well designed nature, any llm provider with langchain support can be used, so OpenAI, Mistral, etc. Provider list with packages here: [LangChain Provider Integrations](https://docs.langchain.com/oss/python/integrations/providers/overview).

Input options are either **audio**, **files**, or **text**. For audio, the user can record themselves, or input an audio file, such as an mp4. For files, the user can input a PDF file, or files such as an html/htm, or text file. For text, the user can simply type in their statement, or copy and paste it in.

The `docs` folder is where the documentation github page is deployed from, it serves only to provide more information about the project, and is not needed to run the project, but reading it via the github page can prove useful.

## Contributing
Contributions to this repository are welcome! If you wish to contribute, please follow the guidelines below.

Heres how you can contribute:
1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push to the branch
5. Submit a pull request


## License
This project is licensed under the Apache 2.0 License - see the [LICENSE](https://github.com/drod75/Lai/blob/main/LICENSE) file for details.

