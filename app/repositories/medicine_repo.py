# app/repositories/medicine_repo.py
from sqlalchemy.orm import Session
from app.models import Medicine

# CRUD operations for medicines
def get_medicines(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Medicine).offset(skip).limit(limit).all()

def get_medicine_by_id(db: Session, medicine_id: int):
    return db.query(Medicine).filter(Medicine.id == medicine_id).first()

def create_medicine(db: Session, name: str, formula: str, purpose: str, box_location: str):
    db_medicine = Medicine(name=name, formula=formula, purpose=purpose, box_location=box_location)  # Changed description to purpose
    db.add(db_medicine)
    db.commit()
    db.refresh(db_medicine)
    return db_medicine
