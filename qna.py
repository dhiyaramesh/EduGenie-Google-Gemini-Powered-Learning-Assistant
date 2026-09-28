def get_qna_answer(question):
    q = question.lower()
    
    if "artificial" in q:
        return """Simulating Human Intelligence: Artificial Intelligence (AI) is technology that enables computers to perform tasks that need human thinking like reasoning and learning.
Learning from Data: Instead of manual programming, AI analyzes massive information to identify patterns and improve.
Problem-Solving and Decision-Making: AI processes complex variables in real-time to calculate the best outcome.
Perception and Understanding: AI can interpret world by seeing through cameras and understanding human language.
Adaptability: AI systems get smarter with more data and usage, becoming more accurate over time."""

    if "machine learning" in q:
        return """Definition: Machine Learning is a subset of AI that learns from data.
Supervised Learning: Learns from labeled examples.
Unsupervised Learning: Finds hidden patterns.
Reinforcement Learning: Learns by trial and error.
Applications: Used in Netflix, Google, self-driving cars."""

    return f"""Ask Anything: You can ask about {question} - I am your EduGenie tutor.
Easy Explanations: I will break down {question} into simple 5 steps.
Homework Help: I can guide you through homework related to this topic.
Learn at Your Pace: We can go as fast or slow as you need.
Get Started: Let's explore {question} together in detail!"""