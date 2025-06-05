import streamlit as st
import requests

API_URL = "http://localhost:8000/travel-assist"

st.set_page_config(page_title="AI Travel Assistant")
st.title("🌍 Personalized AI Travel Assistant")

# 🔹 Input Form
with st.form("travel_form"):
    destination = st.text_input("Where do you want to go?", "Krakow")
    days = st.number_input("How many days will you stay?", min_value=1, max_value=14, value=3)
    interests = st.multiselect(
        "What are you interested in?",
        ["History", "Food", "Nature", "Museums"],
        default=["History"]
    )
    submitted = st.form_submit_button("Generate Plan")

if submitted:
    payload = {
        "destination": destination,
        "days": days,
        "interests": interests
    }

    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            data = response.json()

            # 🌤️ Weather Forecast
            st.markdown("### 🌤️ Weather Forecast")
            weather = data.get("weather", "")
            st.markdown(f"<p style='font-size:16px;'><b>Here is the general weather forecast for your trip:</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size:15px;'>{weather}</p>", unsafe_allow_html=True)

            # 🗺️ Travel Plan
            st.markdown("### 🗺️ Travel Plan")
            readable_city = destination.title()
            readable_focus = ', '.join(interests) if interests else 'General'
            st.markdown(f"<h4>{days}-Day Travel Guide for {readable_city} — Focused on {readable_focus}</h4>", unsafe_allow_html=True)

            plan_text = data.get("plan", "No travel suggestions found.")
            st.markdown(f"<div style='font-size:15px;'>{plan_text}</div>", unsafe_allow_html=True)

            # 🏨 Hotel Suggestions (with cards)
            st.markdown("### 🏨 Hotel Suggestions")
            hotel_list = data.get("hotels", [])

            if hotel_list:
                st.markdown(f"<p style='font-size:16px;'>Recommended places to stay for your <b>{days}-day</b> trip:</p>", unsafe_allow_html=True)

                for i, hotel in enumerate(hotel_list):
                    name = hotel.get("name", "Hotel")
                    rating = hotel.get("rating", "N/A")
                    price = hotel.get("price", "N/A")
                    photo = hotel.get("photo", "")
                    link = hotel.get("link", "")

                    st.markdown(f"""
                    <div style='border:1px solid #ddd; padding:10px; border-radius:10px; margin-bottom:12px; display:flex; gap:12px;'>
                        <img src='{photo}' alt='Hotel Image' style='width:120px; height:90px; object-fit:cover; border-radius:6px;'/>
                        <div>
                            <p style='margin:0; font-weight:bold; font-size:16px;'>{i+1}. {name}</p>
                            <p style='margin:0;'>⭐ <b>{rating}</b> — 💵 ${price}</p>
                            <p style='margin:0;'><a href='{link}' target='_blank'>View on Booking.com</a></p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("No hotel suggestions available.")

        else:
            st.error(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"❌ Failed to connect to backend: {e}")
