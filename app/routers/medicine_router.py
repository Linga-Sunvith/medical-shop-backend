# app/routers/medicine_router.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import Medicine, MedicineCreate
from app.services.medicine_service import fetch_medicines, fetch_medicine_by_id, add_medicine
from app.database import get_db

router = APIRouter()

@router.get("/medicines", response_model=list[Medicine])
def get_medicines(skip: int = 0, limit: int = 10, query: str = None, db: Session = Depends(get_db)):
    if query:
        # If a search query is provided, filter medicines by name using 'ilike' for case-insensitive search
        return db.query(Medicine).filter(Medicine.name.ilike(f"%{query}%")).offset(skip).limit(limit).all()
    return fetch_medicines(db, skip, limit)

# Fetch medicine by ID
@router.get("/medicines/{medicine_id}", response_model=Medicine)
def get_medicine_by_id(medicine_id: int, db: Session = Depends(get_db)):
    return fetch_medicine_by_id(db, medicine_id)

# Add a new medicine
@router.post("/medicines", response_model=Medicine)
def create_medicine(medicine: MedicineCreate, db: Session = Depends(get_db)):
    return add_medicine(db, medicine.name, medicine.formula, medicine.purpose, medicine.box_location)
