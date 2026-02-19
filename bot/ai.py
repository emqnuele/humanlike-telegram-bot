import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=GOOGLE_API_KEY)

HISTORY_DIR = "data/histories"

def load_system_prompt():
    try:
        if os.path.exists("data/system_prompt.txt"):
            with open("data/system_prompt.txt", "r", encoding="utf-8") as f:
                return f.read()
        
        with open("data/system_prompt.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("system_instruction", "You are a helpful assistant.")
    except Exception:
        return "You are a helpful assistant."

def get_history_file(chat_id):
    return os.path.join(HISTORY_DIR, f"{chat_id}.json")

def load_history(chat_id):
    file_path = get_history_file(chat_id)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                return json.load(f).get("history", [])
            except json.JSONDecodeError:
                return []
    return []

def save_history(chat_id, history):
    file_path = get_history_file(chat_id)
    os.makedirs(HISTORY_DIR, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump({"history": history}, f, ensure_ascii=False, indent=2)

def generate_response(chat_id, user_message):
    system_instruction = load_system_prompt()
    history = load_history(chat_id)
        
    contents = []
    for entry in history:
        contents.append(types.Content(
            role=entry["role"],
            parts=[types.Part.from_text(text=p) for p in entry["parts"]]
        ))
    
    contents.append(types.Content(
        role="user",
        parts=[types.Part.from_text(text=user_message)]
    ))

    try:
        response = client.models.generate_content(
            model=os.getenv("GOOGLE_MODEL_NAME", "gemini-2.0-flash"),
            config=types.GenerateContentConfig(
                system_instruction=system_instruction
            ),
            contents=contents
        )
        
        bot_response = response.text

        history.append({"role": "user", "parts": [user_message]})
        history.append({"role": "model", "parts": [bot_response]})
        save_history(chat_id, history)
        
        return bot_response
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Scusa, ho avuto un problema nel processare la tua richiesta."
