from pydantic import BaseModel, EmailStr
from typing import Optional, List
import datetime

class InterviewerCreate(BaseModel):
    name: str
    email: EmailStr
    role: Optional[str]

class InterviewerRead(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: Optional[str]
    active: bool
    created_at: datetime.datetime


    class Config:
        orm_mode = True

class CandidateCreate(BaseModel):
    name: str
    email: Optional[EmailStr]
    phone: Optional[str]
    resume_link: Optional[str]

class CandidateRead(BaseModel):
    id: int
    name: str
    email: Optional[EmailStr]
    phone: Optional[str]
    resume_link: Optional[str]
    created_at: datetime.datetime

    class Config:
        orm_mode = True

class QuestionCreate(BaseModel):
    text: str
    order: Optional[int] = 0

class QuestionRead(BaseModel):
    id: int
    text: str
    order: int

    class Config:
        orm_mode = True

class NoteCreate(BaseModel):
    text: str
    question_id: Optional[int]
    rating: Optional[float]

class NoteRead(BaseModel):
    id: int
    text: str
    created_at: datetime.datetime
    rating: Optional[float]

    class Config:
        orm_mode = True

class InterviewCreate(BaseModel):
    title: str
    description: Optional[str]
    scheduled_at: Optional[datetime.datetime]
    duration_minutes: Optional[int]
    interviewer_id: Optional[int]
    candidate: Optional[CandidateCreate]
    questions: Optional[List[QuestionCreate]] = []

class InterviewRead(BaseModel):
    id: int
    title: str
    description: Optional[str]
    scheduled_at: Optional[datetime.datetime]
    duration_minutes: Optional[int]
    status: str
    overall_rating: Optional[float]
    interviewer: Optional[InterviewerRead]
    candidate: Optional[CandidateRead]
    questions: List[QuestionRead] = []
    notes: List[NoteRead] = []

    class Config:
        orm_mode = True
