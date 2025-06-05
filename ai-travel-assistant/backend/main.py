from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.agents.planner_agent import plan_travel_tasks
from backend.agents.executor_agent import execute_task

app = FastAPI()

# CORS (Streamlit ile bağlantı için şart)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/travel-assist")
async def travel_assist(request: Request):
    data = await request.json()
    destination = data.get("destination", "London")
    days = data.get("days", 3)
    interests = data.get("interests", [])

    tasks = plan_travel_tasks(destination, days, interests)

    results = {}
    for task in tasks:
        result = execute_task(task)
        results[task["type"]] = result

    return {
        "weather": results.get("weather", ""),
        "plan": results.get("plan", ""),
        "hotels": results.get("hotel", []),
        "restaurants": results.get("restaurant", [])
    }
