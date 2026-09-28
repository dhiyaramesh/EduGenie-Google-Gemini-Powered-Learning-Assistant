from google import genai
import os, time
from dotenv import load_dotenv
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODELS = ["gemini-3.8-flash", "gemini-flash-latest", "gemini-pro-latest", "gemini-2.0-flash-lite"]

def get_summary(text):
    for model in MODELS:
        try:
            r = client.models.generate_content(model=model, contents=f"Summarize in 5 bullets: {text}")
            return r.text
        except:
            time.sleep(1)
            continue
    return "busy"