# app/routers/medicine_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.schemas import MedicineCreate, MedicineResponse
from app.services.medicine_service import fetch_medicines, add_medicine, modify_medicine, remove_medicine
from app.database import get_db

router = APIRouter()

@router.get("/medicines", response_model=list[MedicineResponse])
def get_medicines(search_query: str = None, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return fetch_medicines(db, search_query, skip, limit)

@router.post("/medicines", response_model=MedicineResponse)
def create_medicine(medicine: MedicineCreate, db: Session = Depends(get_db)):
    print("recieved medicine data:", medicine)
    return add_medicine(db, medicine.dict())

@router.put("/medicines/{medicine_id}", response_model=MedicineResponse)
def update_medicine(medicine_id: int, medicine: MedicineCreate, db: Session = Depends(get_db)):
    updated_medicine = modify_medicine(db, medicine_id, medicine.dict())
    if not updated_medicine:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return updated_medicine

@router.delete("/medicines/{medicine_id}")
def delete_medicine(medicine_id: int, db: Session = Depends(get_db)):
    deleted_medicine = remove_medicine(db, medicine_id)
    if not deleted_medicine:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return {"message": "Medicine deleted successfully"}
