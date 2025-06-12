from ..database import database_utils
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from pytz import timezone




class Fitness_Classes(database_utils.Base):
    __tablename__ = "fitnessclasses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    date_time = Column(DateTime, nullable=False, index=True)
    instructor = Column(String(50), nullable=False)
    available_slots = Column(Integer, nullable=False)
    

    bookings = relationship("Booking", back_populates="fitness_class")

    def __repr__(self):
        return f"Fitness_Classes({self.id}, {self.name})"


class Client(database_utils.Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String(50), nullable=False)
    client_email = Column(String(50), nullable=False, unique=True)

    bookings = relationship("Booking", back_populates="client")

    def __repr__(self):
        return f"Client({self.id}, {self.client_name}, {self.client_email})"


class Booking(database_utils.Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("fitnessclasses.id"), nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    booked_at = Column(DateTime, index=True, nullable=False)

    fitness_class = relationship("Fitness_Classes", back_populates="bookings")
    client = relationship("Client", back_populates="bookings")

    def __repr__(self):
        return f"Booking({self.id}, Class={self.class_id}, Client={self.client_id}, At={self.booked_at})"
    
    
class BookingHistory(database_utils.Base):
    __tablename__="bookinghistorys"
    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("fitnessclasses.id"), nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    booked_at = Column(DateTime, index=True, nullable=False)
    archived_at = Column(DateTime, default=datetime.now(tz=timezone("Asia/kolkata")))
    
    
    def __repr__(self):
        return f"Booking({self.id}, Class={self.class_id}, Client={self.client_id}, At={self.booked_at}, Archived_at={self.archived_at})"
    