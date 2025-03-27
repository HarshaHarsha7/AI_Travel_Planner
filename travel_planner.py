import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("⚠️ API key is missing! Set GEMINI_API_KEY in your environment or .env file.")
else:
    genai.configure(api_key=GEMINI_API_KEY)

# Function to generate travel itinerary
def generate_travel_itinerary(destination, budget, duration, interests):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Latest working model
        response = model.generate_content(f"Plan a trip to {destination} with a budget of {budget} for {duration} days. Interests: {interests}.")
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="AI Travel Planner", page_icon="✈️", layout="centered")
st.title("🌍 AI-Powered Travel Planner by Harsha ✈️")

# User Inputs
destination = st.text_input("📍 Destination:")
budget = st.text_input("💰 Budget ($):")
duration = st.number_input("📅 Trip Duration (days):", min_value=1, step=1)
interests = st.text_area("🎯 Travel Interests (e.g., beaches, history, food)")

# Generate Itinerary Button
if st.button("📝 Generate Itinerary"):
    if destination and budget and duration and interests:
        itinerary = generate_travel_itinerary(destination, budget, duration, interests)
        st.subheader("🗺 Your AI-Generated Itinerary:")
        st.write(itinerary)
    else:
        st.warning("⚠️ Please fill in all fields before generating an itinerary.")

