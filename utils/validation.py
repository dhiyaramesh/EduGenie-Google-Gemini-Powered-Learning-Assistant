from pydantic import BaseModel, Field
from typing import Optional

class QARequest(BaseModel):
    question: str = Field(..., min_length=1)

class ExplainRequest(BaseModel):
    topic: str = Field(..., min_length=1)

class QuizRequest(BaseModel):
    text: str = Field(..., min_length=1)

class SummaryRequest(BaseModel):
    text: str = Field(..., min_length=1)

class LearningPathRequest(BaseModel):
    topic: str = Field(..., min_length=1)
    level: Optional[str] = Field(None)
