# Phase 5 - Project Development - EduGenie

## Development Approach
Modular development using Flask MVC pattern.

## Folder Structure Implemented
- main.py: Flask app entry point
- learning_path.py: Generates personalized learning roadmap
- explanation_module.py: Gemini-based topic explanation
- qna.py: Doubt clearing module
- quiz_generator: Auto quiz from topic
- templates/index.html: UI
- static/: CSS, JS
- prompts/: System prompts for Gemini

## Key Features Implemented
1. Topic Explanation - Simplified, intermediate, advanced levels
2. QnA Chat - Context-aware answers
3. Quiz Generation - MCQ from any topic
4. Learning Path - Step-by-step roadmap

## Code Integration
- Used google-generativeai library
- Environment variables for API_KEY
- Error handling for API limits

## Challenges Faced & Solved
- Gemini rate limit -> Added retry logic
- Long responses -> Added streaming in frontend
- __pycache__ cleanup -> Added .gitignore

Project fully functional and pushed to GitHub.
