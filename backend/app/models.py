from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class Interviewer(Base):
    __tablename__ = 'interviewers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(String, nullable=True)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


    interviews = relationship('Interview', back_populates='interviewer')

class Candidate(Base):
    __tablename__ = 'candidates'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, index=True)
    phone = Column(String, nullable=True)
    resume_link = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    interviews = relationship('Interview', back_populates='candidate')

class Interview(Base):
    __tablename__ = 'interviews'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    scheduled_at = Column(DateTime, nullable=True)
    duration_minutes = Column(Integer, nullable=True)
    status = Column(String, default='scheduled') # scheduled, completed, cancelled


    interviewer_id = Column(Integer, ForeignKey('interviewers.id'))
    candidate_id = Column(Integer, ForeignKey('candidates.id'))


    interviewer = relationship('Interviewer', back_populates='interviews')
    candidate = relationship('Candidate', back_populates='interviews')


    questions = relationship('Question', back_populates='interview', cascade='all, delete-orphan')
    notes = relationship('Note', back_populates='interview', cascade='all, delete-orphan')


    overall_rating = Column(Float, nullable=True)

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    order = Column(Integer, default=0)
    interview_id = Column(Integer, ForeignKey('interviews.id'))


    interview = relationship('Interview', back_populates='questions')
    notes = relationship('Note', back_populates='question')

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    interview_id = Column(Integer, ForeignKey('interviews.id'), nullable=True)
    question_id = Column(Integer, ForeignKey('questions.id'), nullable=True)
    rating = Column(Float, nullable=True) # optional per-note rating


    interview = relationship('Interview', back_populates='notes')
    question = relationship('Question', back_populates='notes')