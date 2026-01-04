from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import LogQuery
from log_processor import analyze_logs


app = FastAPI()


app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"] ,
allow_headers=["*"] ,
)
@app.post("/analyze")
def analyze(data: LogQuery):
result = analyze_logs(data.logs, data.question)
return result
