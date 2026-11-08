from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Reads OPENAI_API_KEY from your .env file (see .env.example)
client = OpenAI()

# Make the API request
response = client.chat.completions.create(
  model="gpt-6-luna",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is a LLM?"}
  ]
)

# Print the generated text
print(response.choices[0].message.content.strip())
