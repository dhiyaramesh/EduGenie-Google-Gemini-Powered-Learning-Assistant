import os
from dotenv import load_dotenv
load_dotenv()
from google import genai
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_explanation(concept):
    if not concept: return "Please enter a concept!"
    prompt = f"Explain concept '{concept}' in simple words: definition, how it works, example, why important. Use bullet points."
    try:
        resp = client.interactions.create(model="gemini-3.8-flash", input=prompt)
        return resp.output_text
    except Exception as e:
        return f"Error: {e}"