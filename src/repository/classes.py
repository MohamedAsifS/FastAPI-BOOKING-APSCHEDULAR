from fastapi import HTTPException
from ..models import classes_booking
from ..schema import classes
from sqlalchemy.orm import Session



def add_classes(request:classes.Fitness_Classes_schema,db:Session):
    data=classes_booking.Fitness_Classes(**request.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    return {"message":"Data is Cretaed"}
    
def get_classes(db:Session):
    datas=db.query(classes_booking.Fitness_Classes).all()
    if len(datas)<1:
        raise HTTPException(status_code=404,detail="No Instructor Available")
        
    return datas