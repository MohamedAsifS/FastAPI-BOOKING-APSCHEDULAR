from pydantic import BaseModel 
from datetime import datetime


class Fitness_Classes_schema(BaseModel):
    name:str 
    date_time:datetime
    instructor:str 
    available_slots:int
    

    
    
    