from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

class TTSAgent:
    '''
    This class is a simple TTS agent that uses OpenAI's API to generate text-to-speech audio from a given text.
    '''
    def __init__(self):
        self.client = OpenAI()
        self.model = "gpt-4o"
        self.system_prompt = "You are a helpful TTS assistant."
        self.personality = "You will answer questions as if you are a wise old wizard."

    def generate_response(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt + " " + self.personality},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content.strip()
    
    def generate_tts(self, response):
        tts_response = self.client.audio.speech.create(
            model="tts-1",
            voice="onyx",
            response_format="mp3",
            input=response
        )

        speech_file_path = Path(__file__).parent / "speech.mp3"
        tts_response.stream_to_file(speech_file_path)

agent = TTSAgent()

user_prompt = input("You: ")
response = agent.generate_response(user_prompt)
print("AI: " + response)
agent.generate_tts(response)