from backend.rag.external_data import fetch_city_documents
from backend.llm_utils import generate_llm_response
from backend.tools.hotel_tool import get_hotel_suggestions
from backend.tools.weather_tool import get_weather_forecast

def execute_task(task: dict):
    """
    Executes a given subtask based on its type.
    """
    task_type = task.get("type")
    city = task.get("city", "London")
    days = int(task.get("days", 3))
    interests = task.get("interests", [])
    description = task.get("description", "")

    if task_type == "plan":
        docs = fetch_city_documents(city)
        if not docs or not docs[0].get("content"):
            return f"No travel content found for {city}."

        context = "\n".join([d["content"] for d in docs[:3]])

        interest_text = ', '.join(interests) if interests else 'general tourism'
        include_food = "Food" in interests

        food_instruction = (
            "- 🍽️ Include local food suggestions if relevant to the route and interests.\n"
            if include_food else
            "Do NOT include any restaurants, cafes, or food recommendations.\n"
        )

        prompt = (
            f"You are a professional travel assistant AI. Use the following travel guide content as context:\n\n"
            f"{context}\n\n"
            f"Plan a trip to {city}, focused on these interests: {interest_text}.\n"
            f"Your goal is to create a **time-balanced, realistic day-by-day itinerary**.\n\n"
            f"🛑 Only include as many days as needed to fully explore the city — up to a maximum of {days} days.\n"
            f"You may suggest fewer days if appropriate. Do NOT suggest more than {days}.\n\n"
            f"For each day, do the following:\n"
            f"- 📍 Recommend places that can realistically be visited in a day\n"
            f"- 🕒 Include the estimated visit time for each location (e.g., 30 minutes, 2 hours, half-day)\n"
            f"- ⏱️ Ensure that the total daily visit time stays around 6 to 8 hours maximum\n"
            f"- 🎯 Give a short reason for each place\n"
            f"- 🗺️ Recommend the best logical visiting order\n"
            f"{food_instruction}\n"
            f"Format the response in markdown. Use headings like 'Day 1:', 'Day 2:' clearly."
        )

        return generate_llm_response(prompt)

    elif task_type == "hotel":
        count = min(max(2, days), 7)  # Min 2, Max 7 otel
        return get_hotel_suggestions(city, count=count)

    elif task_type == "weather":
        return get_weather_forecast(city)

    else:
        return "Unrecognized task type."
