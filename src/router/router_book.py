from fastapi import FastAPI,APIRouter 

router=APIRouter()

@router.get("/book")
def book():
     pass
 
@router.get("/booking")
def booking():
     pass