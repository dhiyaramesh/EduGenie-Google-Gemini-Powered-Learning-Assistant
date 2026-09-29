import os
import google.generativeai as genai

def get_explanation(topic):
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Explain {topic} in detail")
        return response.text
    except:
        if "computer" in topic.lower():
            return "COMPUTER Detailed Explanation:\n\nDefinition: Computer is an electronic device that takes input, processes it and gives output. Word Computer comes from Compute means calculate.\n\nIPOS Cycle: Input (Keyboard, Mouse), Process (CPU is brain), Output (Monitor, Printer), Storage (RAM, Hard Disk).\n\nTypes: 1. Supercomputer (Fastest, for ISRO, NASA), 2. Mainframe (Banks), 3. Mini, 4. Micro (Laptop, Desktop).\n\nComponents: Hardware (physical parts) and Software (Windows, Apps).\n\nImportance: Used in Education, Banking, Hospital, Business, Railway booking. Most important invention of 20th century."
        else:
            return f"{topic} Detailed Explanation:\n\nDefinition: {topic} is an important concept in education that students must learn.\n\nHow it works: It involves basic principles, types, and real-world applications. Step by step learning makes it easy.\n\nTypes: Different types of {topic} based on use and size.\n\nExamples: Used in daily life, industry, technology.\n\nImportance: Very useful for exams, career and future.\n\nConclusion: Mastering {topic} helps in both academic and practical life."