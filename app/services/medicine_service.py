# app/services/medicine_service.py
from sqlalchemy.orm import Session
from app.repositories.medicine_repo import (
    get_medicines as repo_get_medicines,
    create_medicine as repo_create_medicine,
    update_medicine as repo_update_medicine,
    delete_medicine as repo_delete_medicine,
)

def fetch_medicines(db: Session, search_query: str = None, skip: int = 0, limit: int = 10):
    return repo_get_medicines(db, search_query, skip, limit)

def add_medicine(db: Session, medicine_data: dict):
    return repo_create_medicine(db, medicine_data)

def modify_medicine(db: Session, medicine_id: int, medicine_data: dict):
    return repo_update_medicine(db, medicine_id, medicine_data)

def remove_medicine(db: Session, medicine_id: int):
    return repo_delete_medicine(db, medicine_id)
