import os
import subprocess
import streamlit as st

# Install ollama only if it's not already installed
try:
    import ollama
except ImportError:
    subprocess.run(["pip", "install", "ollama"])
    import ollama  # Import after installation

# Function to generate travel itinerary
def generate_travel_itinerary(destination, budget, duration, interests):
    try:
        response = ollama.chat(
            model="mistral",
            messages=[
                {
                    "role": "user",
                    "content": f"Plan a trip to {destination} with a budget of {budget} for {duration} days. Interests: {interests}"
                }
            ]
        )
        return response["message"]["content"]
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="AI Travel Planner", page_icon="✈️", layout="centered")
st.title("🌍 AI-Powered Travel Planner ✈️")

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
