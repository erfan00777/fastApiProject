from fastapi import FastAPI
from app.routers import router
from app.helper import *
app = FastAPI()

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    create_table()
    alter_table()


@app.on_event("shutdown")
async def shutdown_event():
    close_clients()


