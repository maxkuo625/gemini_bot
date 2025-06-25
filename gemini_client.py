import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def chat_with_gemini(user_input, history=None):
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat(history=history or [])
    response = chat.send_message(user_input)
    return response.text


