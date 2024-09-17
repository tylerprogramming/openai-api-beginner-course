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

### Installing OpenAI Python Library:

```bash
pip install openai
```

### Setting Up the API Key:

Create a `.env` file in the root of your project and add your OpenAI API key:

```bash
OPENAI_API_KEY=sk-proj-1111
```

### Installing dotenv:

```bash
pip install python-dotenv
```

### Importing the API Key:

```bash
from dotenv import load_dotenv
load_dotenv()
``` 


# Models we can call:

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
- It uses the `gpt-4o-mini` model.
- It uses the `conversation_history` to keep track of the chat history.
- It uses the `client.chat.completions.create` method to generate responses.

#### At the most basic level, we are sending a prompt to the model and receiving a response in a while loop until the user types 'exit'.


## Documents:
- [models](https://platform.openai.com/docs/models)