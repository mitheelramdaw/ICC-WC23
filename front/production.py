import streamlit as st 

st.title("Cricket player predictions🏏")

st.title("Weather")
st.write("The weather predictions for today")

selection = st.radio("Select the weather conditions:", ["Sunny☀️", "Overcast⛅", "Drizzle🌦️", "Rain🌧️"])

# Display the selected weather condition
st.write(f"Selected weather condition: {selection}")

st.title("Forms.")
st.write("See stats for your players")

st.title("Pitch Conditions")
st.write("Below you will find pitch conditions")

search_query = st.text_input("Search Player information")
