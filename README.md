# Lesson 1: Introduction to OpenAI API and AI Agents

## 1. Introduction to AI Agents

### What are AI agents?
AI agents are programs designed to interact with their environment, make decisions, and perform tasks autonomously. They often use APIs to retrieve or send data.

### Examples of AI agents in the real world:

- Chatbots for customer support
- Personal assistants like Siri or Alexa
- Agents for automating tasks like email sorting or scheduling meetings

### Key Concepts:

- **Autonomy**: Agents can perform tasks without constant user input
- **Interactivity**: They interact with humans or other systems (like APIs)
- **Decision-Making**: They can make decisions based on data or user inputs

## 2. Introduction to OpenAI API

### What is OpenAI API?
OpenAI API provides powerful models that can understand and generate human language. It allows developers to build apps that leverage natural language processing (NLP), text generation, and more.

### Key Features:

- Text completion: Generate text based on a given prompt
- Conversational agents: Create bots that can engage in human-like conversations
- Code generation: Generate code snippets based on instructions

### API Use Cases:

- Writing assistants (e.g., Grammarly-like apps)
- Personalized recommendations
- Automated customer service agents

### How to Use OpenAI API:

Make an API call using Python (or another language), send a prompt, and receive a response.

## 3. Prerequisites

- Basic knowledge of Python (variables, functions)
- An OpenAI account and API key (signup at [OpenAI API](https://openai.com/api/))

## 4. Setting Up the Environment

### Installing Python and pip:
Ensure you have Python installed on your machine, along with pip to install libraries.

### Installing the Python libraries:

```bash
pip install -r requirements.txt
```

This installs `openai` (3.x) and `python-dotenv`. Python 3.10 or newer is required.

### Setting Up the API Key:

Copy `.env.example` to `.env` in the root of the project and put your OpenAI API key in it:

```bash
OPENAI_API_KEY=sk-proj-1111
```

Every script calls `load_dotenv()`, so the key is read from `.env`. Never paste a real key into a script.

### Importing the API Key:

```bash
from dotenv import load_dotenv
load_dotenv()
``` 


# Models we can call:

> **Model update (November 2026):** the list below is from when the course was recorded (September 2024). OpenAI has since retired or scheduled shutdowns for most of these models; see the [deprecations page](https://developers.openai.com/api/docs/deprecations). The scripts now use:
> - `gpt-6-luna` for chat and vision (scripts 01-04, 06). It replaces `gpt-4o` and `gpt-4o-mini`, which shut down on January 14, 2027.
> - `gpt-transcribe` for speech-to-text (script 07). It replaces `whisper-1`, which shuts down on February 26, 2027.
> - `tts-1` for text-to-speech (scripts 05, 06) still works until January 6, 2027. Its replacement, `gpt-realtime-2.1-mini`, only runs on the Realtime API, not `/v1/audio/speech`, so these two lessons will need a rewrite after that date.

- GPT-4o	Our high-intelligence flagship model for complex, multi-step tasks
- GPT-4o mini	Our affordable and intelligent small model for fast, lightweight tasks
- o1-preview and o1-mini	Language models trained with reinforcement learning to perform complex reasoning.
- GPT-4 Turbo and GPT-4	The previous set of high-intelligence models
- GPT-3.5 Turbo	A fast, inexpensive model for simple tasks
- DALL·E	A model that can generate and edit images given a natural language prompt
- TTS	A set of models that can convert text into natural sounding spoken audio
- Whisper	A model that can convert audio into text
- Embeddings	A set of models that can convert text into a numerical form
- Moderation	A fine-tuned model that can detect whether text may be sensitive or unsafe
- GPT base	A set of models without instruction following that can understand as well as generate natural language or code


# 03 - simple chatbot.py

- This is a simple chatbot that uses the OpenAI API to generate responses to user prompts.
- It uses the `gpt-6-luna` model (the original recording used `gpt-4o-mini`).
- It uses the `conversation_history` to keep track of the chat history.
- It uses the `client.chat.completions.create` method to generate responses.

#### At the most basic level, we are sending a prompt to the model and receiving a response in a while loop until the user types 'exit'.


# 04 - simple agent.py

- This is a simple agent that uses the OpenAI API to generate responses to user prompts.
- We create a class called `SimpleAgent` that has a `generate_response` method that takes a prompt and returns a response.
- We give it a personality and a system prompt.
- It uses the `gpt-6-luna` model (the original recording used `gpt-4o-mini`).
- It uses the `conversation_history` to keep track of the chat history.
- It uses the `client.chat.completions.create` method to generate responses.

#### This is a very simple agent, but it shows the power of the OpenAI API.

# 05 - TTS (text-to-speech)
- This is a simple TTS app that uses the OpenAI API to convert text to speech.
- It uses the `tts-1` model.
- It uses the `client.audio.speech.create` method to generate speech.
- It uses the `speech_file_path` to save the speech to a file.
- It uses the `response.stream_to_file` method to save the speech to a file.

## Documents:
- [models](https://platform.openai.com/docs/models)