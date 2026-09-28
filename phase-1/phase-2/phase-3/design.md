# Phase-3: Project Design
Architecture:
User (index.html) -> FastAPI routes (main.py) -> Modules (explanation_module.py, quiz_module.py, qna.py, learning_path.py) -> Gemini API -> Response to User

Flow:
1. User enters topic
2. Frontend calls /explain, /quiz, /ask, /learning-path
3. Backend calls Gemini
4. Result shown on UI
