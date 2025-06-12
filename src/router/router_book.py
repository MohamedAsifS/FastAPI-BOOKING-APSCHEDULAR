from fastapi import FastAPI,APIRouter,Depends

from sqlalchemy.orm import Session
from..database import database_utils
from ..repository import repo_book
from ..schema import schema_book as book_schema
from typing import List
from ..logging import logging


router=APIRouter()

@router.post("/book",status_code=201,tags=['Client'])
def booker(request:book_schema.ClientSchema,db:Session=Depends(database_utils.get_db)):
     logging.info("Book API is called by client to book the class ")
     return repo_book.book(db,request)
     
 
@router.get("/booking",response_model=List[book_schema.BookingSchema],tags=['Client'])
def booking(email:str,db:Session=Depends(database_utils.get_db)):
     logging.info("Usr checks his current upcoming booking")
     return repo_book.get_all_book(db,email)

@router.get("/book_all",response_model=List[book_schema.BookingHistorySchema],tags=['Admin'])
def all_booking_data(db:Session=Depends(database_utils.get_db)):
     logging.info("Previous book history API is called")
     return repo_book.previous_data(db)