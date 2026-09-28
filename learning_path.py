import os
from dotenv import load_dotenv
load_dotenv()
from google import genai
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_learning_path(goal):
    if not goal: return "Please enter what you want to learn!"
    prompt = f"Create a 4-week learning path for: {goal}. Give Week 1, Week 2, Week 3, Week 4 with topics, tasks, resources."
    try:
        resp = client.interactions.create(model="gemini-3.8-flash", input=prompt)
        return resp.output_text
    except Exception as e:
        return f"Error: {e}"