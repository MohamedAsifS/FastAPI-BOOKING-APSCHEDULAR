from fastapi import HTTPException
from pytz import timezone
from ..models import classes_booking
from ..schema import schema_classes
from sqlalchemy.orm import Session
from datetime import datetime

ist=timezone("Asia/kolkata")



def add_classes(request:schema_classes.Fitness_Classes_schema,db:Session):
    local=ist.localize(request.date_time)
  
    data=request.dict()
    data["date_time"]=local
    data=classes_booking.Fitness_Classes(**data)
    db.add(data)
    db.commit()
    db.refresh(data)
    return {"message":f"Classes is added {request.name} and instrcutor {request.instructor}"}
    
def get_classes(db:Session):
    datas=db.query(classes_booking.Fitness_Classes).all()
    if len(datas)<1:
        raise HTTPException(status_code=404,detail="No Instructor Available")
    filter_data=[]
    for data in datas:
        if ist.localize(data.date_time)>datetime.now(tz=ist):
            filter_data.append(data)
    return filter_data