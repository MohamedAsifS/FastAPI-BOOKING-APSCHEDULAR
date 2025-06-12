from pydantic import BaseModel,EmailStr
from .schema_classes import Fitness_Classes_schema
from typing import List
from datetime import datetime

class ClientSchema(BaseModel):
    id:int 
    client_name:str 
    client_email:EmailStr
    
class ClientSchemaResponse(ClientSchema):
    class config():
        orm_mode=True
    
class FitnessClassSchema(BaseModel):
    name: str
    date_time: datetime
    instructor: str
    available_slots: int

    class Config:
        orm_mode = True

class BookingSchema(BaseModel):
    id: int
    booked_at: datetime
    fitness_class: FitnessClassSchema

    class Config:
        orm_mode = True
class BookingHistorySchema(BaseModel):
    id:int
    class_id:int 
    client_id:int 
    booked_at:datetime 
    archived_at:datetime
    
    
    class config:
        orm_mode=True