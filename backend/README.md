A minimal FastAPI backend to manage interviewers, interviews, candidates, questions, notes and ratings. Uses SQLAlchemy + SQLite by default.

Run:


```bash
pip install -r requirements.txt
export DATABASE_URL="sqlite:///./interviewer.db"
uvicorn app.main:app --reload
```