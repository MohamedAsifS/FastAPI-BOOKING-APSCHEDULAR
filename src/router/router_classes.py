from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from ..repository import repo_classes
from ..schema.schema_classes import Fitness_Classes_schema
from ..database.database_utils import get_db
from ..logging import logging
router=APIRouter()

@router.get("/classes",status_code=200,tags=['Client'])
def get_classes(db:Session=Depends(get_db)):
    logging.info("Clinet checks the available classes")
    return repo_classes.get_classes(db)

@router.post("/classes",status_code=201,tags=['Admin'])
def add_classes(request:Fitness_Classes_schema,db:Session=Depends(get_db)):
   logging.info("new fitness class is added")
   return repo_classes.add_classes(request,db)