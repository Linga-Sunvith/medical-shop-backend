from pydantic import BaseModel

class MedicineBase(BaseModel):
    name: str
    formula: str
    purpose: str
    box_location: str

class MedicineCreate(MedicineBase):
    pass

class MedicineResponse(MedicineBase):
    id: int

    class Config:
        from_attributes = True

