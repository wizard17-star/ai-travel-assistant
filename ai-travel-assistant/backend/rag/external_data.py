import requests
import os

def fetch_city_documents(city, source="wikipedia"):
    """
    Fetches travel-related content for a city from the selected API.
    Returns a list of {'title': ..., 'content': ...} dictionaries.
    """
    if source == "wikipedia":
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{city}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return [{
                "title": data.get("title", city),
                "content": data.get("extract", f"No summary available for {city}.")
            }]
        else:
            return [{"title": city, "content": f"No data available for {city}."}]
    
    elif source == "opentripmap":
        # OpenTripMap Example (API key required)
        api_key = os.getenv("OPENTRIPMAP_API_KEY")
        # Get city coordinates
        geo_url = f"https://api.opentripmap.com/0.1/en/places/geoname?name={city}&apikey={api_key}"
        geo_response = requests.get(geo_url)
        if geo_response.status_code != 200:
            return [{"title": city, "content": "No geolocation found."}]
        geo_data = geo_response.json()
        lat, lon = geo_data.get("lat"), geo_data.get("lon")
        # Get places of interest
        poi_url = (f"https://api.opentripmap.com/0.1/en/places/radius"
                   f"?radius=2000&lon={lon}&lat={lat}&limit=10&apikey={api_key}")
        poi_response = requests.get(poi_url)
        if poi_response.status_code != 200:
            return [{"title": city, "content": "No POIs found."}]
        pois = poi_response.json().get("features", [])
        docs = []
        for poi in pois:
            name = poi["properties"].get("name", "Unknown Place")
            kind = poi["properties"].get("kinds", "unknown")
            docs.append({
                "title": name,
                "content": f"{name} is a place of interest in {city} (type: {kind})."
            })
        return docs if docs else [{"title": city, "content": f"No POIs found for {city}."}]
    
    
    
    else:
        return [{"title": city, "content": f"No data source matched for {city}."}]
