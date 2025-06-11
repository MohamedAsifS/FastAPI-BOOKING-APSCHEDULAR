from fastapi import FastAPI 
from .database import database_utils 
from .router.classes import router
from .scheduler import schedulers_utils

database_utils.Base.metadata.create_all(bind=database_utils.engine)

app=FastAPI()
app.include_router(router)



# @app.on_event("startup")
# def start():
#     schedulers_utils.bc.start()
#     print("Application and Schedular started")

# @app.on_event("shutdown")
# def close():
#     schedulers_utils.bc.shutdown()
#     print("Application Stopped and Scheduler stopped")