import os
import google.generativeai as genai

def get_learning_path(topic):
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Create a detailed 4-week learning path for {topic} with daily topics, resources, projects"
        response = model.generate_content(prompt)
        return response.text
    except:
        t = topic.upper()
        if "computer" in topic.lower():
            return f"""LEARNING PATH for {t} - 4 Week Plan:

**WEEK 1: Basics**
Day 1-2: What is Computer? History, Generations
Day 3-4: Types of Computer - Super, Mainframe, Micro
Day 5-7: Components - Input, Output, CPU, Memory
Project: Draw block diagram of Computer

**WEEK 2: Intermediate**
Day 8-10: Hardware vs Software, OS - Windows, Linux
Day 11-13: MS Office - Word, Excel, PowerPoint
Day 14: Internet Basics, Email, Browser
Project: Create PPT on Computer

**WEEK 3: Advanced**
Day 15-17: Networking, Types of Networks
Day 18-20: Programming Intro - Python/C
Day 21: Cybersecurity basics
Project: Make simple calculator in Python

**WEEK 4: Expert + Career**
Day 22-24: AI, Cloud, Data Science intro
Day 25-27: Real projects - Build website/app
Day 28: Revision + Mock Interview
Career: Software Engineer, Data Analyst, IT Support

Resources: YouTube (CodeWithHarry), W3Schools, GeeksForGeeks
"""
        else:
            return f"""LEARNING PATH for {t} - 4 Week Complete Plan:

**WEEK 1: Foundation**
Day 1-2: Introduction to {t} - Definition, History
Day 3-4: Importance and Scope of {t}
Day 5-7: Basic Terms and Concepts of {t}
Task: Read 2 articles on {t} daily

**WEEK 2: Core Concepts**
Day 8-10: Main principles and How {t} works
Day 11-13: Types and Classifications of {t}
Day 14: Important Examples of {t}
Task: Make notes + Mind Map

**WEEK 3: Practical**
Day 15-17: Real-world Applications of {t}
Day 18-20: Tools and Technologies related to {t}
Day 21: Mini Project on {t}
Task: Build small project

**WEEK 4: Mastery**
Day 22-24: Advanced topics in {t}
Day 25-27: Interview Questions on {t}
Day 28: Final Revision + Test
Career Options: Jobs related to {t} are very high demand

Resources: YouTube, Google, Books on {t}
Tip: Practice 1 hour daily!
"""