from google import genai
import os, time
from dotenv import load_dotenv
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODELS = ["gemini-3.8-flash", "gemini-flash-latest", "gemini-pro-latest", "gemini-2.0-flash-lite"]

def get_explanation(topic):
    for model in MODELS:
        try:
            r = client.models.generate_content(model=model, contents=f"Explain {topic} in 5 simple points with examples")
            return r.text
        except:
            time.sleep(1)
            continue
    return "busy"