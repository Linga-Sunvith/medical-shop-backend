# app/services/medicine_service.py
from sqlalchemy.orm import Session
from app.repositories.medicine_repo import get_medicines, get_medicine_by_id, create_medicine

# Fetch medicines from the database
def fetch_medicines(db: Session, skip: int = 0, limit: int = 10):
    return get_medicines(db, skip, limit)

# Fetch a single medicine by ID
def fetch_medicine_by_id(db: Session, medicine_id: int):
    return get_medicine_by_id(db, medicine_id)

# Add a new medicine
def add_medicine(db: Session, name: str, formula: str, purpose: str, box_location: str):
    return create_medicine(db, name, formula, purpose, box_location)  # Changed description to purpose

