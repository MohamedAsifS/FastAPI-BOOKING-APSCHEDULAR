from apscheduler.schedulers.background import BackgroundScheduler 
from pytz import timezone
from sqlalchemy.orm import Session 
from ..models import classes_booking
from fastapi import Depends
from datetime import datetime,timedelta
from ..database import database_utils
from ..logging import logging



bc=BackgroundScheduler(timezone=timezone("Asia/Kolkata"))

def reset_db(classes):
    db:Session=database_utils.session()
    try:
        
                data=db.query(classes_booking.Fitness_Classes).filter(classes_booking.Fitness_Classes.name==classes).first()
           
                logging.info(f"Databse reset started for {classes}")
                data.available_slots=50
                current_time=data.date_time.time()
                date=datetime.now(tz=timezone("Asia/Kolkata"))
                data.date_time=datetime.combine(date,current_time)+timedelta(days=1)
               
                db.commit()
                logging.info(f"row updated for {classes}")
    finally:
        db.close()

def booking_migrater():
    db:Session=database_utils.session()
    try:
        logging.info("migrater starts")
        datas=db.query(classes_booking.BookingHistory).all()
        count=len(datas)
        count+=1
        print(count)
        for data in datas:
            print(data)
            db.add(classes_booking.BookingHistory(id=count,class_id=data.class_id,client_id=data.client_id,booked_at=data.booked_at,archived_at=datetime.now(tz=timezone("Asia/kolkata"))))
            db.commit()
            db.refresh(data)
            count+=1
        db.query(classes_booking.Booking).delete()
        db.commit()
        logging.info("table migrated and booking table reseted")
    finally:
        db.close()
            
            

bc.add_job(func=reset_db,trigger="cron",hour=7,minute=0,args=['Yoga'])
bc.add_job(func=reset_db,trigger="cron",hour=10,minute=30,args=['HIIT'])
bc.add_job(func=reset_db,trigger="cron",hour=18,minute=0,args=['Zumba'])
bc.add_job(func=booking_migrater,trigger='cron',minute=0,hour=0)

