from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from datetime import datetime
from db.database import Base

class Message(Base):
    __tablename__ = "messages"

    message_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    name = Column(String(150), nullable=False)  
    email = Column(String(150), nullable=False)  
    subject = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    create_date = Column(DateTime, default=datetime.utcnow)