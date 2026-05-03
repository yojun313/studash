from fastapi import FastAPI
from app.routes.student_routes import router as student_router
import uvicorn
import os
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="StuDash")

os.makedirs("app/static/profiles", exist_ok=True)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(student_router)