from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Load your OpenAI API key
client = OpenAI()

conversation_history = []

while True:
    prompt = input("You: ")

    conversation_history.append({"role": "user", "content": prompt})

    if prompt.lower() == 'exit':
        break
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"You are a helpful assistant, you will answer the user's questions as Shakespeare would.  The chat history context: {conversation_history}"},
            {"role": "user", "content": prompt}
            ]
        )

        print("AI: " + response.choices[0].message.content.strip())
        conversation_history.append({"role": "assistant", "content": response.choices[0].message.content.strip()})
    except client.error.OpenAIError as e:
        print("Error: " + str(e))
