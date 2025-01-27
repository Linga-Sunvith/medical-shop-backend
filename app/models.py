from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Medicine(Base):
    __tablename__ = 'medicines'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    formula = Column(Text, nullable=False)
    purpose = Column(Text, nullable=False)
    box_location = Column(String(50), nullable=False)
