from fastapi import FastAPI
from resources.user import router as user_router
from resources.process import router as process_router
from resources.payment import router as payment_router
from resources.process_status import router as process_status_router

from database import init_db

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["users"])
app.include_router(process_router, prefix="/process", tags=["process"])
app.include_router(payment_router, prefix="/payment", tags=["payment"])
app.include_router(process_status_router, prefix="/process_status", tags=["process_status"])


@app.on_event("startup")
def on_startup():
    init_db()
