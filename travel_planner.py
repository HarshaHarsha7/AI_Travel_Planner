import streamlit as st
import ollama

def generate_travel_itinerary(destination, budget, duration, interests):
    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": f"Plan a trip to {destination} with a budget of {budget} for {duration} days. Interests: {interests}"}]
    )
    return response["message"]["content"]

# Streamlit UI
st.title("🌍 AI-Powered Travel Planner ✈️")

destination = st.text_input("Enter your destination:")
budget = st.text_input("Enter your budget:")
duration = st.number_input("Enter trip duration (in days):", min_value=1, step=1)
interests = st.text_area("What are your travel interests? (e.g., beaches, history, food)")

if st.button("Generate Itinerary"):
    if destination and budget and duration and interests:
        itinerary = generate_travel_itinerary(destination, budget, duration, interests)
        st.subheader("🗺 Your AI-Generated Itinerary:")
        st.write(itinerary)
    else:
        st.warning("Please fill in all fields before generating an itinerary.")
