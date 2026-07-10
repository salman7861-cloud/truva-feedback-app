from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import Feedback

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Truva Feedback App")

frontend_dir = Path(__file__).resolve().parent.parent / "frontend"
app.mount("/static", StaticFiles(directory=frontend_dir), name="static")


class FeedbackCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    message: str = Field(min_length=1)


@app.get("/")
def read_root():
    return FileResponse(frontend_dir / "index.html")


@app.post("/api/feedback", status_code=status.HTTP_201_CREATED)
def create_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    name = feedback.name.strip()
    message = feedback.message.strip()

    if not name or not message:
        raise HTTPException(status_code=400, detail="Name and message are required")

    new_feedback = Feedback(name=name, message=message)
    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)

    return {"id": new_feedback.id, "name": new_feedback.name, "message": new_feedback.message}


@app.get("/api/feedback")
def list_feedbacks(db: Session = Depends(get_db)):
    feedbacks = db.query(Feedback).order_by(Feedback.id.desc()).all()
    return [{"id": item.id, "name": item.name, "message": item.message} for item in feedbacks]
