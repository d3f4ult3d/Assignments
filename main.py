from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class match_stats(BaseModel):
    runs : int
    overs: float
    target : int

@app.post("/required_run_rate")
def required_run_rate(stats: match_stats):
    ballsCompleted = (int(stats.overs)*6) + (round(stats.overs*10)%10)
    runs_needed = stats.target - stats.runs
    ballsLeft = 120 - ballsCompleted
    if (ballsLeft>0):
        Orrr = (runs_needed/ballsLeft)*6 
    else:
        Orrr = 0
    rrr = round(Orrr, 2)
    return{
       "Required Run Rate": rrr 
    }

@app.get("/")
def api_status():
    return{
        "message":"API IS LIVE"
    }

@app.get("/health")
def health():
    return{
        "status":"ok"
    }