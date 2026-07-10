from sqlalchemy import Column, Integer, String, Text

from .database import Base


class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    message = Column(Text, nullable=False)
