# app/repositories/medicine_repo.py
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.models import Medicine

def get_medicines(db: Session, search_query: str = None, skip: int = 0, limit: int = 10):
    query = db.query(Medicine)
    if search_query:
        query = query.filter(
            or_(
                Medicine.name.ilike(f"%{search_query}%"),
                Medicine.formula.ilike(f"%{search_query}%"),
                Medicine.purpose.ilike(f"%{search_query}%"),
            )
        )
    return query.offset(skip).limit(limit).all()

# def create_medicine(db: Session, medicine_data: dict):
#     medicine = Medicine(**medicine_data)
#     db.add(medicine)
#     db.commit()
#     db.refresh(medicine)
#     return medicine
def create_medicine(db: Session, medicine_data: dict):
    try:
        print("Attempting to create medicine with:", medicine_data)
        medicine = Medicine(**medicine_data)
        db.add(medicine)
        db.commit()
        print("Commit successful!")
        db.refresh(medicine)
        print("Refreshed medicine:", medicine)
        return medicine
    except Exception as e:
        db.rollback()
        print("Error in create_medicine:", e)
        raise

def update_medicine(db: Session, medicine_id: int, updated_data: dict):
    medicine = db.query(Medicine).filter(Medicine.id == medicine_id).first()
    if not medicine:
        return None
    for key, value in updated_data.items():
        setattr(medicine, key, value)
    db.commit()
    db.refresh(medicine)
    return medicine

def delete_medicine(db: Session, medicine_id: int):
    medicine = db.query(Medicine).filter(Medicine.id == medicine_id).first()
    if medicine:
        db.delete(medicine)
        db.commit()
        return medicine
    return None
