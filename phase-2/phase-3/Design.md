# Phase-3: Project Design
Architecture:
User (index.html) -> FastAPI routes (main.py) -> Modules -> Gemini API -> Response

Flow:
1. User enters topic
2. Frontend calls /explain, /quiz, /ask, /learning-path
3. Backend calls Gemini
4. Result shown on UI
