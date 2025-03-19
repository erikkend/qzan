import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')


class GeminiAPI:
    def __init__(self):
        self.messages = []

    async def generate_text(self, request_message: str) -> str:
        self.messages.append(
            {'role': 'user', 'parts': [f'{request_message}']}
        )
        response = model.generate_content(self.messages)

        await self.save_response(response.text)
        return response.text

    async def save_response(self, text: str):
        self.messages.append(
            {'role': 'model', 'parts': [text]}
        )

    async def clear_messages(self):
        self.messages.clear()
