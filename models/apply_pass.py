from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from datetime import datetime
from db.database import Base

class ApplyPass(Base):
    __tablename__ = "apply_pass"

    pass_id = Column(Integer, primary_key=True, index=True)
    
    user_id = Column(Integer,ForeignKey("users.user_id"),nullable=False)

    pass_type = Column(String, nullable=False)
    id_proof = Column(String, nullable=False)
    valid_from = Column(Date, nullable=False)
    valid_till = Column(Date, nullable=False)
    create_date = Column(DateTime, default=datetime.utcnow)

