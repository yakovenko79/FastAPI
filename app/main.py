from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from starlette.responses import JSONResponse
from app.models.models import Feedback

app = FastAPI()
lst = []


@app.post("/feedback")
async def add_user(feedback: Feedback):
    lst.append({"name": feedback.name, "comments": feedback.message})
    return f"Feedback received. Thank you, {feedback.name}"


@app.get('/comments')
async def show_feedback():
    return lst
