from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from ..repository import classes
from ..schema.classes import Fitness_Classes_schema
from ..database.database_utils import get_db
router=APIRouter()

@router.get("/classes")
def get_classes(db:Session=Depends(get_db)):
    return classes.get_classes(db)

@router.post("/classes",status_code=201)
def add_classes(request:Fitness_Classes_schema,db:Session=Depends(get_db)):
   return classes.add_classes(request,db)