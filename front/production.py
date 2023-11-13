import streamlit as st

# Main title
st.title("Player Predictions")

# Search bar in the main page
search_query = st.text_input("Search Player information")
if search_query:
    st.write(f"Search results for: {search_query}")

# Page selection buttons
weather_button = st.button("Weather")
form_button = st.button("Forms")
pitch_conditions_button = st.button("Pitch Conditions")

# Display information based on button clicks
if weather_button:
    st.title("Weather")
    st.write("The weather predictions for today")

    # Allow user to input weather condition
    custom_condition = st.text_input("Enter the weather condition:")

    # Display information based on user input
    if custom_condition:
        st.write(f"The weather condition is: {custom_condition}")
    else:
        st.write("No custom weather condition entered.")

elif form_button:
    st.title("Forms.")
    st.write("See stats for your players")

elif pitch_conditions_button:
    st.title("Pitch Conditions")
    st.write("Below you will find pitch conditions")
