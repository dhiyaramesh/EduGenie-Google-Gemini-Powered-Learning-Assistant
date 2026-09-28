import os
from dotenv import load_dotenv
load_dotenv()
from google import genai
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_quiz(topic):
    if not topic: return "Please enter a topic!"
    prompt = f"""Create 5 MCQ quiz on topic: {topic}
    Format exactly:
    Q1. Question?
    A) option B) option C) option D) option
    Answer: A
    Explanation: short
    (Repeat for 5 questions)"""
    try:
        resp = client.interactions.create(model="gemini-3.8-flash", input=prompt)
        return resp.output_text
    except Exception as e:
        return f"Error: {e}"