from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

class STTAgent:
    '''
    This class is a simple STT agent that uses OpenAI's API to generate speech-to-text from a given audio file.
    '''
    def __init__(self, audio_file_name: str, text_file_name: str):
        self.client = OpenAI()
        self.model = "whisper-1"
        self.audio_folder = Path(__file__).parent / "audio"
        self.audio_file_name = audio_file_name
        self.audio_file_path = self.audio_folder / self.audio_file_name
        self.text_folder = Path(__file__).parent / "text"
        self.text_file_name = text_file_name
        self.text_file_path = self.text_folder / self.text_file_name

    def transcribe_audio(self) -> str:
        self.create_audio_file_path()
        self.create_text_file_path()

        with open(self.audio_file_path, "rb") as audio_file:
            transcription = self.client.audio.transcriptions.create(
                model=self.model,
                file=audio_file
            )

        return transcription.text
    
    def create_text_file(self):
        self.create_text_file_path()
        with open(self.text_file_path, "w") as text_file:
            text_file.write(self.transcribe_audio())
    
    def create_audio_file_path(self):
        audio_folder = Path(__file__).parent / "audio"
        audio_folder.mkdir(exist_ok=True)

    def create_text_file_path(self):
        text_folder = Path(__file__).parent / "text"
        text_folder.mkdir(exist_ok=True)

stt_agent = STTAgent("audio.mp3", "audio.txt")
transcription = stt_agent.transcribe_audio()
stt_agent.create_text_file()
        