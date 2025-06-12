from ..database import database_utils 
from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..schema.schema_book import ClientSchema
from ..models import classes_booking
from pytz import timezone 
from datetime import datetime
from email_validator import validate_email,EmailNotValidError
from ..logging import logging

def email_validated_error(email):
    try:
        validate_email(email)
        return True 
    except EmailNotValidError:
        return False 
    except Exception:
        return False


def client_creater(name,email,db:Session):
    logging.info("Clinet is new and start to creating")
    create=classes_booking.Client(client_name=name,client_email=email)
    db.add(create)
    db.commit()
    db.refresh(create)
    logging.info(f"{create.client_name} is created")
    return "Clinet is Created he/she is new"

def minus_the_slot(id:int,db:Session):
    get_data=db.query(classes_booking.Fitness_Classes).filter(classes_booking.Fitness_Classes.id==id).first()
    minus_slot=get_data.available_slots-1
    update_data=get_data.available_slots=minus_slot
    db.commit()
    logging.info("Slot is updated")

def restrict_user_for_overbooking(db:Session,client_id,class_id):
    query=db.query(classes_booking.Booking).filter(classes_booking.Booking.client_id==client_id,classes_booking.Booking.class_id==class_id).first()
    print(query,class_id)
    if query :
        logging.error("Email registed for this slot and session")
        raise HTTPException(status_code=400,detail="Your Email Already Registered for this class and slot (one user with email can book only one slot)")
    
    
    
    
    

def book(db:Session,request:ClientSchema):
      if not email_validated_error(request.client_email):
          logging.error("invalid Email")
          raise HTTPException(status_code=422,detail="Email is invlaid ")
          
      check_slots=db.query(classes_booking.Fitness_Classes).filter(classes_booking.Fitness_Classes.id==request.id).first()
      if not check_slots:
          logging.error("There is no classes in databse where requested by client")
          raise HTTPException(status_code=404,detail="Class Not Found")
      
      now=datetime.now(tz=timezone("Asia/kolkata"))
      time_from_db=timezone("Asia/kolkata").localize(check_slots.date_time)
      if time_from_db<now:
          logging.error("Very extreme edge case where user can;t book")
          raise HTTPException(status_code=409,detail="Can't book, class booking time exceeded")
      
     
      if check_slots.available_slots<1:
          logging.error("slots are filled")
          raise HTTPException(status_code=409,detail="No slots available")
      
      
      check_clinet=db.query(classes_booking.Client).filter(classes_booking.Client.client_email==request.client_email).first()
      if not check_clinet:
          client_creater(request.client_name,request.client_email,db)
          
          
      minus_the_slot(request.id,db) 
      
      get_clinet=db.query(classes_booking.Client).filter(classes_booking.Client.client_email==request.client_email).first()
      
      restrict_user_for_overbooking(db,get_clinet.id,check_slots.id)
      
      booking=classes_booking.Booking(class_id=check_slots.id,client_id=get_clinet.id,booked_at=now)
      db.add(booking)
      db.commit()
      db.refresh(booking)
      logging.info(f"Session is Booked  for {check_slots.name} at {check_slots.date_time} by {get_clinet.client_name}")
      return f"Session is Booked  for {check_slots.name} at {check_slots.date_time}  ,thanks {get_clinet.client_name}"
      
          
      
def get_all_book(db:Session,email:str):
   
   results= db.query(classes_booking.Booking).join(classes_booking.Client, classes_booking.Booking.client_id == classes_booking.Client.id).filter(classes_booking.Client.client_email == email).all()    
   
   return results

def previous_data(db:Session):
    results=db.query(classes_booking.BookingHistory).all()
    print(results)
    return results
    

