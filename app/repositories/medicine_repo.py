# app/repositories/medicine_repo.py
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.models import Medicine
import logging

logger = logging.getLogger("medical-shop-backend")

def get_filtered_medicines(db: Session, search_query: str = None, skip: int = 0, limit: int = 10):
    try:
        query = db.query(Medicine)
        if search_query:
            query = query.filter(
                or_(
                    Medicine.name.ilike(f"%{search_query}%"),
                    Medicine.formula.ilike(f"%{search_query}%"),
                    Medicine.purpose.ilike(f"%{search_query}%")
                )
            )
        return query.offset(skip).limit(limit).all()
    except Exception as e:
        logger.error(f"Error in get_filtered_medicines: {e}")
        raise

def create_medicine(db: Session, medicine: Medicine):
    try:
        db.add(medicine)
        db.commit()
        db.refresh(medicine)
        return medicine
    except Exception as e:
        logger.error(f"Error in create_medicine: {e}")
        raise

def update_medicine(db: Session, medicine_id: int, updated_data: dict):
    try:
        db_medicine = db.query(Medicine).filter(Medicine.id == medicine_id).first()
        if not db_medicine:
            return None
        for key, value in updated_data.items():
            setattr(db_medicine, key, value)
        db.commit()
        db.refresh(db_medicine)
        return db_medicine
    except Exception as e:
        logger.error(f"Error in update_medicine: {e}")
        raise

def delete_medicine(db: Session, medicine_id: int):
    try:
        db_medicine = db.query(Medicine).filter(Medicine.id == medicine_id).first()
        if db_medicine:
            db.delete(db_medicine)
            db.commit()
        return db_medicine
    except Exception as e:
        logger.error(f"Error in delete_medicine: {e}")
        raise
