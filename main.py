from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
load_dotenv()

from qna import get_qna_answer
from explanation_module import get_explanation
from quiz_module import get_quiz
from summary_module import get_summary
from learning_path import get_learning_path

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.post("/ask")
def ask(question: str = Form(...)):
    try:
        ans = get_qna_answer(question)
        if not ans or "busy" in ans.lower():
            return {"answer": "Google 3.8 is very busy. WAIT 15 SECONDS and click Get Answer AGAIN - it will auto-switch to backup model and work!"}
        return {"answer": ans}
    except Exception as e:
        print(e)
        return {"answer": "AI busy (503). Please wait 10 sec and try again. Backup model will take over."}

@app.post("/explain")
def explain(topic: str = Form(...)):
    try:
        return {"answer": get_explanation(topic)}
    except:
        return {"answer": "Busy, try again after 10 sec."}

@app.post("/quiz")
def quiz(topic: str = Form(...)):
    try:
        return {"answer": get_quiz(topic)}
    except:
        return {"answer": "Busy, try again after 10 sec."}

@app.post("/summarize")
def summarize(text: str = Form(...)):
    try:
        return {"answer": get_summary(text)}
    except:
        return {"answer": "Busy, try again after 10 sec."}

@app.post("/learning-path")
def learning_path(goal: str = Form(...)):
    try:
        return {"answer": get_learning_path(goal)}
    except:
        return {"answer": "Busy, try again after 10 sec."}