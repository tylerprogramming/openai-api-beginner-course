from openai import OpenAI

# Load your OpenAI API key
client = OpenAI(api_key="sk-proj-1111")

# Make the API request
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is a LLM?"}
  ]
)

# Print the generated text
print(response.choices[0].message.content.strip())
