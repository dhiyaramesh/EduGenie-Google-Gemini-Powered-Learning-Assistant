# EduGenie — Google Gemini Powered Learning Assistant

> A lightweight, AI-powered educational web application built with FastAPI and Google Gemini.
> SmartBridge / Naan Mudhalvan College Project.

---

## Features

| Feature | Endpoint | Description |
|---|---|---|
| **Ask a Question** | `POST /qa` | Get clear, student-friendly answers to any academic question |
| **Explain a Concept** | `POST /explain` | Structured beginner explanation with definition, steps, and example |
| **Generate Quiz** | `POST /quiz` | 3 MCQs with 4 options each, correct answer, and explanation |
| **Summarize Text** | `POST /summarize` | Concise revision-ready summary of any educational passage |
| **Learning Path** | `POST /learn/recommendations` | Personalized beginner-to-advanced roadmap with practice suggestions |

---

## Technology Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.10+, FastAPI, Uvicorn |
| **AI Model** | Google Gemini 1.5 Flash (via `google-generativeai`) |
| **Frontend** | HTML5, CSS3, JavaScript (Fetch API) |
| **Templating** | Jinja2 |
| **Config** | python-dotenv |

---

## Folder Structure

```
EduGenie-SmartBridge/
├── main.py                    # FastAPI application and all routes
├── qna.py                     # Q&A module
├── explanation_module.py      # Concept explanation module
├── quiz_module.py             # Quiz generation module
├── summary_module.py          # Text summarization module
├── learning_path.py           # Learning path module
├── templates/
│   └── index.html             # Single-page frontend
├── static/
│   ├── style.css              # Responsive CSS styling
│   └── script.js              # Frontend JavaScript (fetch, quiz logic)
├── .env                       # Your API key (NOT committed to Git)
├── .env.example               # Template for .env
├── .gitignore                 # Excludes .env and cache files
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

---

## Prerequisites

- **Python 3.10 or higher**
  Verify: `python --version`

- **A Google Gemini API Key** (free)
  Get one at: https://aistudio.google.com/app/apikey

- **Internet connection** (Gemini is a cloud API)

---

## Installation

### 1. Clone or download the project

```
cd EduGenie-SmartBridge
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

## API Key Setup

### Step 1: Copy the example file

```
copy .env.example .env
```

### Step 2: Open `.env` and add your key

```
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

> The `.env` file is listed in `.gitignore` and will never be committed to version control.
> Never share or hardcode your API key in source files.

---

## How to Run

```
uvicorn main:app --reload
```

Then open your browser and go to:

```
http://127.0.0.1:8000
```

The API documentation (Swagger UI) is available at:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

| Method | Endpoint | Request Body | Response |
|---|---|---|---|
| `GET` | `/` | — | HTML frontend page |
| `POST` | `/qa` | `{ "question": "string" }` | `{ "answer": "string" }` |
| `POST` | `/explain` | `{ "topic": "string" }` | `{ "explanation": "string" }` |
| `POST` | `/quiz` | `{ "text": "string" }` | `{ "quiz": [ ... ] }` |
| `POST` | `/summarize` | `{ "text": "string" }` | `{ "summary": "string" }` |
| `POST` | `/learn/recommendations` | `{ "topic": "string" }` | `{ "recommendations": "string" }` |

### Error Response Format

All errors return:
```json
{ "detail": "Descriptive error message" }
```

---

## How to Use Each Feature

### Ask a Question
1. Click the **Ask a Question** tab
2. Type your academic question in the text area
3. Click **Get Answer**
4. The AI-generated answer appears below

**Example:** `What is artificial intelligence?`

---

### Explain a Concept
1. Click the **Explain a Concept** tab
2. Enter the concept you want explained
3. Click **Explain It**
4. Receive a structured explanation: definition, easy explanation, step-by-step breakdown, and real-world example

**Example:** `Database normalization`

---

### Generate Quiz
1. Click the **Generate Quiz** tab
2. Enter a topic name or paste an educational passage
3. Click **Generate Quiz**
4. Three multiple-choice questions appear with four options each
5. Select your answers and click **Check Answers** to see your score, correct answers, and explanations

**Example:** `Python functions`

---

### Summarize Text
1. Click the **Summarize Text** tab
2. Paste a long educational passage into the text area
3. Click **Summarize**
4. A concise, revision-ready summary appears

**Example:** Paste any textbook paragraph or Wikipedia excerpt

---

### Learning Path
1. Click the **Learning Path** tab
2. Enter a subject you want to learn
3. Click **Get Learning Path**
4. Receive a structured roadmap: overview, beginner/intermediate/advanced topics, learning sequence, practice suggestions, and resource types

**Example:** `Python programming`

---

## Testing

Run the built-in test suite:

```
python -c "
import sys
sys.path.insert(0, '.')
import os, json, unittest.mock as mock
os.environ['GEMINI_API_KEY'] = 'test'
mg = mock.MagicMock()
mr = mock.MagicMock()
mr.text = 'Test response'
mg.GenerativeModel.return_value.generate_content.return_value = mr
sys.modules['google.generativeai'] = mg
import main
from fastapi.testclient import TestClient
c = TestClient(main.app)
r = c.post('/qa', json={'question': 'test'})
print('QA:', r.status_code, r.json())
r = c.get('/')
print('UI:', r.status_code)
"
```

Or test manually through the Swagger UI at `http://127.0.0.1:8000/docs`.

---

## Troubleshooting

| Problem | Solution |
|---|---|
| `GEMINI_API_KEY is not set` | Create a `.env` file with your API key (see API Key Setup above) |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `uvicorn: command not found` | Run `python -m uvicorn main:app --reload` instead |
| Quiz returns parse error | Try a different or more specific topic; the AI occasionally returns malformed JSON |
| Empty or short responses | Check your internet connection; Gemini is a cloud API |
| `port already in use` | Stop any other server on port 8000 or use `--port 8001` |

---

## Security Notes

- The Gemini API key is stored only in the `.env` file — never in any source file
- `.env` is listed in `.gitignore` and must never be committed to version control
- The API key is never sent to the browser or exposed in frontend JavaScript
- No user input or AI responses are stored or logged by the application
- The application is designed for local use (`127.0.0.1`); do not expose it to the public internet without adding authentication and HTTPS

---

*EduGenie — SmartBridge / Naan Mudhalvan College Project*

## 📹 Demo Video
https://drive.google.com/file/d/YOUR_VIDEO_LINK/view?usp=sharing

## 🔗 GitHub Repository
https://github.com/dhiyaramesh/EduGenie-Google-Gemini-Powered-Learning-Assistant

## 👩‍💻 Project Created By
Dhiya Ramesh - Final Year Project - Naan Mudhalvan / SmartBridge

## ✅ Project Phases Completed
- phase-1: Ideation
- phase-2: Requirement Analysis  
- phase-3: Project Design (with 5 Architecture Diagrams)
- phase-4: Project Planning
- phase-5: Development (Flask + Gemini API)
- phase-6: Testing
