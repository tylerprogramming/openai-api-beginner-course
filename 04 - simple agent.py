from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class SimpleAgent:
    def __init__(self):
        self.client = OpenAI()
        self.conversation_history = []
        self.model = "gpt-4o-mini"
        self.system_prompt = "You are a helpful assistant."
        self.personality = "You will answer questions as if you are a wise old wizard."

    def generate_response(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt + " " + self.personality + " The conversation history is: " + str(self.conversation_history)},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content.strip()

    def add_to_conversation_history(self, role, content):
        self.conversation_history.append({"role": role, "content": content})

    def get_conversation_history(self):
        return self.conversation_history

agent = SimpleAgent()

while True:
    prompt = input("You: ")
    response = agent.generate_response(prompt)
    print("AI: " + response)
    agent.add_to_conversation_history("user", prompt)
    agent.add_to_conversation_history("assistant", response)

    if prompt.lower() == 'exit':
        break