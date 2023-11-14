import streamlit as st
import requests

# Function to display the homepage
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

# Function to display cricket predictions
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

# Function to get live scores from the cricket API
def get_live_scores():
    api_key = '8ecd14c1-8c1e-460c-b365-2d48e412c7b8'
    base_url = 'https://api.cricapi.com/v1/currentMatches'
    
    params = {
        'apikey': api_key,
        'offset': 0
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        try:
            data = response.json()
            return data.get('data', [])
        except Exception as e:
            print(f'Error decoding JSON: {e}')
            return []
    else:
        print(f'Error fetching data. Status code: {response.status_code}')
        return []

# Function to display live cricket scores
def display_live_cricket_scores():
    st.title('Live Cricket Scores')

    # Get live scores
    live_scores = get_live_scores()

    if live_scores:
        st.markdown('**Live Cricket Scores:**')

        for match in live_scores:
            st.markdown(
                f"""
                <div style="
                    border: 5px solid #fff;
                    border-radius: 10px;
                    padding: 15px;
                    margin-bottom: 20px;
                    background-color: #000000;
                ">
                    <p style="font-size: 26px; font-weight: bold; color: #fff;">{match['name']}</p>
                    <p style="font-size: 20px;"><strong>Status:</strong> {match['status']}</p>
                    <p style="font-size: 20px;"><strong>Venue:</strong> {match['venue']}</p>
                    <p style="font-size: 20px;"><strong>Date and Time:</strong> {match['date']} ({match['dateTimeGMT']})</p>
                    <p style="font-size: 20px;"><strong>Teams:</strong> {', '.join(match['teams'])}</p>
                    <p style="font-size: 20px;"><strong>Result:</strong> {match.get('status', 'No result available')}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.write('No live scores available at the moment.')

# Main function to run the app
def main():
    # Sidebar navigation
    nav_option = st.sidebar.selectbox("Select Section", ["Homepage", "Cricket Predictions", "Live Cricket Scores"])

    if nav_option == "Homepage":
        display_homepage()
    elif nav_option == "Cricket Predictions":
        display_cricket_predictions()
    elif nav_option == "Live Cricket Scores":
        display_live_cricket_scores()

if __name__ == "__main__":
    main()
