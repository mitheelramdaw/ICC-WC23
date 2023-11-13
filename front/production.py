import streamlit as st 

st.title("Cricket player predictions🏏")

search_query = st.text_input("Search Player information")

st.title("Weather")

selection = st.radio("Select the weather conditions:", ["Sunny☀️", "Overcast⛅", "Drizzle🌦️", "Rain🌧️"])


st.write(f"Selected weather condition: {selection}")

st.title("Forms")

selected_form = st.slider("Select player form:", 0, 100, 50, step=10, format="%d%%")

if 0 <= selected_form <=40:
    
    performance_category = "Struggling😭😭😭😭"
elif 50 <= selected_form <= 70:
    performance_category = "Solid😄😄😄😄😄"
elif 80 <= selected_form <= 100:
    performance_category = "World Class😁😁😁😁😁"
else:
    performance_category = "Unknown"
    
st.write(f"Selected form: {selected_form}%")
st.write(f"Player Perfomance Category: {performance_category}")

st.title("Pitch Conditions")
st.write("Below you will find pitch conditions")

selection = st.radio("Select the weather conditions:", ["Soft", "Dry", "Hard", "Grass"])
st.write(f"The pitch condition is: {selection}")


