from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.router.chat_router import router
from openai import OpenAI
import os


app = FastAPI()

# 프론트 연결 허용 (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "FastAPI server running"}

app.include_router(router)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))