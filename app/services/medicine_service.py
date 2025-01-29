# app/services/medicine_service.py
from sqlalchemy.orm import Session
from app.repositories.medicine_repo import (
    get_filtered_medicines,
    create_medicine,
    update_medicine,
    delete_medicine,
)
from app.models.models import Medicine

def fetch_medicines(db: Session, search_query: str = None, skip: int = 0, limit: int = 10):
    return get_filtered_medicines(db, search_query, skip, limit)

def add_medicine(db: Session, medicine_data: dict):
    medicine = Medicine(**medicine_data)
    return create_medicine(db, medicine)

def modify_medicine(db: Session, medicine_id: int, updated_data: dict):
    return update_medicine(db, medicine_id, updated_data)

def remove_medicine(db: Session, medicine_id: int):
    return delete_medicine(db, medicine_id)
