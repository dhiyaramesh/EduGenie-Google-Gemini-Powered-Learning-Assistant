from google import genai
import os, time
from dotenv import load_dotenv
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODELS = ["gemini-3.8-flash", "gemini-flash-latest", "gemini-pro-latest", "gemini-2.0-flash-lite"]

def get_qna_answer(question):
    for _ in range(2):
        for model in MODELS:
            try:
                print(f"Trying {model}")
                r = client.models.generate_content(model=model, contents=f"Answer in detail: {question}")
                return r.text
            except Exception as e:
                print(f"Failed {model}: {e}")
                time.sleep(1)
                continue
        time.sleep(2)
    return "busy - please retry after 10 sec"