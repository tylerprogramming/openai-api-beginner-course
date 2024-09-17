from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o",
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
  max_tokens=300,
)

print(response.choices[0].message.content)