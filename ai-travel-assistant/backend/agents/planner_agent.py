def plan_travel_tasks(destination: str, days: int, interests: list = []):
    """
    Decompose the user request into subtasks for agents to process.
    """
    tasks = [
        {
            "type": "plan",
            "description": f"Create a {days}-day travel plan for {destination}, focused on {', '.join(interests) if interests else 'general interests'}.",
            "city": destination,
            "days": days,
            "interests": interests
        },
        {
            "type": "hotel",
            "description": f"Find suitable hotels in {destination}.",
            "city": destination
        },
        {
            "type": "restaurant",
            "description": f"Find recommended restaurants in {destination}.",
            "city": destination
        },
        {
            "type": "weather",
            "description": f"Get the weather forecast for {destination}.",
            "city": destination
        }
    ]
    return tasks
