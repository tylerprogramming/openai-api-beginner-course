from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-6-luna",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://media.istockphoto.com/id/1137961063/photo/large-group-of-different-animals.jpg?s=612x612&w=0&k=20&c=9CGuSImc5dvYYXHKE3oN1AgsB6pVQdnXnudt6Mambp4=",
          },
        },
      ],
    }
  ],
  # GPT-6 models take max_completion_tokens instead of max_tokens. With
  # reasoning off, the whole budget goes to the visible answer.
  reasoning_effort="none",
  max_completion_tokens=300,
)

print(response.choices[0].message.content)