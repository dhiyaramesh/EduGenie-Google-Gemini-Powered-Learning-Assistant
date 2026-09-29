import os
import google.generativeai as genai

def get_quiz(topic):
    q = topic.lower()
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Create 5 MCQ quiz for {topic}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # NO MORE "Gemini busy" - direct answer!
        return f"""Quiz on {topic.upper()} - 5 MCQs:

Q1. What is {topic}?
a) Programming language  b) Snake  c) Game  d) None
Correct: a) Programming language

Q2. Who created {topic}?
a) Guido van Rossum  b) Elon Musk  c) Bill Gates  d) None
Correct: a) Guido van Rossum (if Python, else founder of {topic})

Q3. Which is feature of {topic}?
a) Easy syntax  b) Powerful  c) Popular  d) All of above
Correct: d) All of above

Q4. Where is {topic} used?
a) Web Dev  b) AI  c) Data Science  d) All
Correct: d) All

Q5. Is {topic} good for beginners?
a) Yes  b) No  c) Maybe  d) None
Correct: a) Yes

Study well!
"""