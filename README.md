# 🧭 AI Travel Assistant

**AI Travel Assistant** is a personalized trip planner that recommends sightseeing spots, hotels, and restaurants based on the destination, travel date, and selected preferences. Powered by multiple APIs and LLM agents, the system generates context-aware suggestions including cultural, culinary, and nature-based attractions.

---

## 🚀 Features

- 🗓️ Suggests sightseeing places (museums, nature, historical sites) based on the selected **city** and **travel date**
- 🏨 Provides hotel recommendations based on destination and budget
- 🍽️ If **Food** is selected, gives restaurant suggestions near attraction points
- ☁️ Fetches **real-time weather data** for selected date and destination
- 🌍 Utilizes a mix of structured APIs and unstructured data (Wikipedia) to enhance recommendations
- 🎯 All-in-one experience in a single-page Streamlit interface
- 🤖 Modular FastAPI backend for flexibility and scalability

---

## 🛠️ Tech Stack

| Layer      | Tools/Services                                         |
|------------|--------------------------------------------------------|
| Frontend   | Streamlit                                              |
| Backend    | FastAPI                                                |
| AI Model   | OpenAI GPT-4 (via OpenAI API)                          |
| Travel Data| OpenTripMap API (attractions)                          |
| Weather    | OpenWeather API                                        |
| Hotels     | Booking.com (via RapidAPI)                             |
| Knowledge  | Wikipedia search                                       |

---

🛠 Project Structure 

<pre> ```bash ai-travel-assistant/ ├── app.py # Streamlit UI ├── executor.py # Core planner logic ├── services/ # Modular service-based API layers │ ├── hotel_service.py │ ├── restaurant_service.py │ ├── weather_service.py │ └── attraction_service.py ├── prompts/ # Custom LLM prompt templates ├── data/ # RAG-style text files ├── .env.example └── requirements.txt ``` </pre>

---

## 🔑 Required API Keys

Create a `.env` file and include the following keys:

```env
OPENAI_API_KEY=your-openai-api-key
OPENTRIPMAP_API_KEY=your-opentripmap-key
OPENWEATHER_API_KEY=your-openweather-key
RAPIDAPI_KEY=your-rapidapi-key

--- 
⚙️ How to Run

# Clone and enter the project
git clone -b serhat https://github.com/wizard17-star/ai-travel-assistant.git
cd ai-travel-assistant

# Set up environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add environment variables
cp .env.example .env
# Edit the .env file and add your keys

# Launch Streamlit frontend
streamlit run app.py
