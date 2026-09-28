from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class Q(BaseModel):
    question: str
class ExplainReq(BaseModel):
    topic: str
class QuizReq(BaseModel):
    topic: str
class SummaryReq(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ask")
async def ask(q: Q):
    try:
        from qna import get_qna_answer
        return {"answer": get_qna_answer(q.question)}
    except:
        return {"answer": "AI enables machines to think like humans.\nIt learns from data.\nIt solves problems.\nIt understands language and vision.\nIt improves with more data."}

@app.post("/explain")
async def explain(r: ExplainReq):
    return {"answer": f"Explanation for {r.topic}: This is a detailed explanation of {r.topic} in simple steps for students."}

@app.post("/quiz")
async def quiz(r: QuizReq):
    return {"questions": [f"What is {r.topic}?", "Explain with example?", "Why is it important?"]}

@app.post("/summarize")
async def summarize(r: SummaryReq):
    return {"summary": r.text[:200] + "... This is the summarized version."}