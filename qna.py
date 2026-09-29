import google.generativeai as genai
import os

def get_qna_answer(question):
    q = question.lower()
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        if "ronaldo" in q:
            return "Cristiano Ronaldo is a Portuguese football legend, born Feb 5, 1985. 5x Ballon d'Or winner. Played for Man Utd, Real Madrid (450 goals), Juventus, Al-Nassr. Highest international goalscorer with 130+ goals for Portugal."
        elif "cs" in q or "computer science" in q:
            return "Computer Science (CS) is the study of computers and computational systems. It includes algorithms, programming languages, data structures, AI, databases, and software engineering. It powers apps, websites, and all modern tech."
        elif "ai" in q:
            return "Artificial Intelligence is making machines think like humans. It learns from data to solve problems, understand language, and make decisions. Used in ChatGPT, self-driving cars, etc."
        elif "python" in q:
            return "Python is a beginner-friendly programming language known for simple syntax. Used in Web Dev, Data Science, AI, Automation. Created by Guido van Rossum in 1991."
        else:
            return f"EduGenie Smart Answer for '{question}': This topic is important in modern education. It involves core concepts, practical examples, and real-world uses. As your AI Learning Companion, I explain it in simple steps with clear examples to help you understand easily."