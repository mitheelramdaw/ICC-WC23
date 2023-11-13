import streamlit as st

def display_homepage():
    st.title("Welcome to Your Simple Homepage")
    
    st.write(
        "This is a simple homepage created using Streamlit. You can customize it "
        "to display the content you want. Feel free to add more sections and "
        "make it your own!"
    )

    st.header("About Us")
    st.write(
        "We are a fantastic team working on exciting projects. Our mission is to "
        "create awesome things and make the world a better place."
    )

    st.header("Latest News")
    st.write(
        "Stay tuned for the latest updates and news. Exciting things are happening "
        "all the time, and we want to share them with you!"
    )

    st.header("Contact Us")
    st.write(
        "Have questions or want to get in touch with us? Reach out to us at "
        "contact@example.com. We would love to hear from you!"
    )

def display_cricket_predictions():
    st.title("Cricket player predictions🏏")

    search_query = st.text_input("Search Player information")

    st.title("Weather")
    selection = st.radio("Select the weather conditions:", ["Sunny☀️", "Overcast⛅", "Drizzle🌦️", "Rain🌧️"])
    st.write(f"Selected weather condition: {selection}")

    st.title("Forms")
    selected_form = st.slider("Select player form:", 0, 100, 50, step=10, format="%d%%")

    if 0 <= selected_form <= 40:
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
    pitch_condition = st.radio("Select the pitch conditions:", ["Soft", "Dry", "Hard", "Grass"])
    st.write(f"The pitch condition is: {pitch_condition}")

def main():
    # Sidebar navigation
    nav_option = st.sidebar.selectbox("Select Section", ["Homepage", "Cricket Predictions"])

    if nav_option == "Homepage":
        display_homepage()
    elif nav_option == "Cricket Predictions":
        display_cricket_predictions()

if __name__ == "__main__":
    main()
