from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import router
from app.helper import *
app = FastAPI()

# CORS middleware setup (optional)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Adjust as needed
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# Include the router
app.include_router(router)

@app.on_event("startup")
async def startup_event():
    create_table()
    # alter_table()


@app.on_event("shutdown")
async def shutdown_event():
    close_clients()


