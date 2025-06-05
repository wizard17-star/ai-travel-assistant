def get_hotel_suggestions(city: str, count: int = 3):
    import requests
    import os
    from dotenv import load_dotenv

    load_dotenv()

    RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
    RAPIDAPI_HOST = "booking-com.p.rapidapi.com"

    try:
        # Koordinat alma
        geo_url = "https://booking-com.p.rapidapi.com/v1/hotels/locations"
        geo_query = {"name": city, "locale": "en-us"}

        headers = {
            "X-RapidAPI-Key": RAPIDAPI_KEY,
            "X-RapidAPI-Host": RAPIDAPI_HOST,
        }

        geo_resp = requests.get(geo_url, headers=headers, params=geo_query)
        geo_data = geo_resp.json()

        if not geo_data:
            return []

        lat = geo_data[0]["latitude"]
        lon = geo_data[0]["longitude"]

        # Otel verisi alma
        hotel_url = "https://booking-com.p.rapidapi.com/v1/hotels/search-by-coordinates"
        hotel_query = {
            "longitude": lon,
            "latitude": lat,
            "locale": "en-us",
            "checkin_date": "2025-07-01",
            "checkout_date": "2025-07-02",
            "adults_number": "1",
            "order_by": "popularity",
            "units": "metric",
            "room_number": "1",
            "filter_by_currency": "USD",
            "page_number": "0",
        }

        hotel_resp = requests.get(hotel_url, headers=headers, params=hotel_query)
        hotel_data = hotel_resp.json()

        hotels = []
        for h in hotel_data.get("result", [])[:count]:
            hotels.append({
                "name": h.get("hotel_name", "Unnamed"),
                "rating": h.get("review_score", "N/A"),
                "price": h.get("min_total_price", "N/A"),
                "photo": h.get("main_photo_url", ""),
                "link": h.get("url", "")
            })

        return hotels

    except Exception as e:
        return [{"name": "Error fetching hotel data", "rating": "", "price": "", "photo": "", "link": "", "error": str(e)}]
