from apscheduler.schedulers.background import BackgroundScheduler 
from pytz import timezone
from sqlalchemy.orm import Session 
from ..models import classes_booking
from fastapi import Depends
from datetime import datetime,timedelta
from ..database import database_utils



bc=BackgroundScheduler(timezone=timezone("Asia/Kolkata"))

def reset_db():
    db:Session=database_utils.session()
    try:
        
           datas=db.query(classes_booking.Fitness_Classes).all()
           for data in datas:
                data.available_slots=50
                current_time=data.date_time.time()
                date=datetime.now(tz=timezone("Asia/Kolkata"))
                data.date_time=datetime.combine(date,current_time)
                # print(date)
                # print(current_time)
                # print(data.date_time)
           db.commit()
    finally:
        db.close()

bc.add_job(func=reset_db,trigger="cron",minute='*')

