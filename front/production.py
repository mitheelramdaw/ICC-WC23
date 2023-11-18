# Import necessary libraries
import streamlit as st
import requests
import pandas as pd
import xgboost as xgb
import numpy as np

# Function to load and preprocess the training data
def load_training_data():
    try:
        # Try to load data from the CSV file
        data = pd.read_csv("data.csv")
        st.write("Data loaded from data.csv.")
    except FileNotFoundError:
        # If the file is not found, fetch data from an alternative source
        st.warning("data.csv not found. Fetching data from alternative source...")
        #data = fetch_data_from_alternative_source()  # This function is not defined in the provided code
        st.write("Data fetched from alternative source and saved to data.csv.")
    
    # Convert categorical pitch condition to numerical values
    data['pitch_condition_numerical'] = data['pitch_condition'].map(
        {"Soft": 1, "Dry": 2, "Hard": 3, "Grass": 4}
    )

    return data

# Function to train the prediction model using XGBoost
def train_prediction_model(data):
    # Features (X) and target variable (y)
    X = data[['form', 'pitch_condition_numerical']]
    y = data['performance']

    # Use XGBoost Regressor instead of LightGBMRegressor
    model = xgb.XGBRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Make predictions on the test set
    y_pred = model.predict(X)

    # Evaluate the model
    mse = np.mean((y - y_pred) ** 2)
    st.write(f"Mean Squared Error on Test Set: {mse}")

    return model

# Function to predict player performance
def predict_performance(model, selected_form, pitch_condition):
    # Convert pitch condition to numerical value
    pitch_condition_numerical = 1 if pitch_condition == "Soft" else 2 if pitch_condition == "Dry" else 3 if pitch_condition == "Hard" else 4

    # Make a prediction using the trained model
    predicted_performance = model.predict(pd.DataFrame({'form': [selected_form], 'pitch_condition_numerical': [pitch_condition_numerical]}))[0]

    return predicted_performance

# Function to display the homepage
def display_homepage():
    # Set the background color to a cricket-themed color
    st.markdown(
        """
        <style>
            body {
                background-color: #006400;  /* Dark green color for a cricket field theme */
                font-family: 'Verdana', sans-serif;  /* Use a clean and widely supported font */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Set the title with a cricket-themed color and styling
    st.title("Welcome to Cricket Central 🏏")
    st.markdown(
        """
        <style>
            h1 {
                color: #FFD700;  /* Gold color for the title */
                text-align: center;  /* Center align the title */
                padding-top: 20px;  /* Add padding at the top */
                font-size: 3em;  /* Increase font size for emphasis */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Introduction and information about the cricket hub
    st.write(
        "Explore the world of cricket with Cricket Central. Your go-to place for all things cricket! "
        "From live scores to player predictions, we've got it all. Let the cricketing journey begin!"
    )

    # Cricket-themed divider line
    st.markdown(
        """
        <hr style="border: 2px solid #FFD700;">
        """,
        unsafe_allow_html=True
    )

    # About Us section with a cricket touch
    st.header("About Cricket Central 🌐")

    # Set the header color and font size
    st.markdown(
        """
        <style>
            h2 {
                color: #FFD700;  /* Gold color for headers */
                font-size: 2.5em;  /* Increase font size for emphasis */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.write(
        "Cricket Central is fueled by passion for the game. We strive to bring you the latest insights, "
        "statistics, and predictions in the world of cricket. Join us on this cricketing adventure!"
    )

    # Latest Cricket News section with a cricket flavor
    st.header("Latest Cricket News 📰")

    # Set the header color and font size
    st.markdown(
        """
        <style>
            h2 {
                color: #FFD700;  /* Gold color for headers */
                font-size: 2.5em;  /* Increase font size for emphasis */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.write(
        "Stay updated with the most recent happenings in the cricketing world. From thrilling matches to "
        "player highlights, we've got the scoop on all things cricket. Don't miss a beat, stay informed!"
    )

    # Cricket-themed divider line
    st.markdown(
        """
        <hr style="border: 2px solid #FFD700;">
        """,
        unsafe_allow_html=True
    )

    # Add a cricket-themed image or logo with rounded corners
    st.image("../images/208410959-cricket-ball-and-bat-on-green-field-with-blue-sky-background.jpg", caption="Cricket Central Logo", use_column_width=True, output_format='PNG')

    # Add some attractive cricket graphics or banners
    st.image("../images/1088609.webp", use_column_width=True, output_format='PNG')
    #st.image("path/to/attractive_cricket_banner_2.png", use_column_width=True, output_format='PNG')

    # Additional cricket-themed sections
    st.header("Cricket Highlights 🏏🌟")

    # Set the header color and font size
    st.markdown(
        """
        <style>
            h2 {
                color: #FFD700;  /* Gold color for headers */
                font-size: 2.5em;  /* Increase font size for emphasis */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.image("../images/highlights.png", use_column_width=True, output_format='PNG')
    st.write(
        "Relive the best moments in cricket history. From iconic sixes to match-winning wickets, "
        "experience the thrill of cricket highlights at Cricket Central."
    )

    st.header("Cricket Stats and Analysis 📊")

    # Set the header color and font size
    st.markdown(
        """
        <style>
            h2 {
                color: #FFD700;  /* Gold color for headers */
                font-size: 2.5em;  /* Increase font size for emphasis */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.image("../images/stats.jpeg", use_column_width=True, output_format='PNG')
    st.write(
        "Dive deep into the numbers and analysis of cricket. Explore player statistics, team performance, "
        "and trends that shape the game. Cricket Central brings you comprehensive cricket insights."
    )

    # Cricket-themed divider line
    st.markdown(
        """
        <hr style="border: 2px solid #FFD700;">
        """,
        unsafe_allow_html=True
    )

    # Additional cricket-themed sections (customize and add more as needed)
    st.header("Fantasy Cricket 🏆")

    st.image("../images/fantasy.jpeg", use_column_width=True, output_format='PNG')
    st.write(
        "Immerse yourself in the world of fantasy cricket. Build your dream team, score points, and compete "
        "with cricket fans worldwide. Cricket Central brings you the ultimate fantasy cricket experience."
    )

    st.header("Cricket Merchandise 🛍️")

    st.image("../images/merch.jpg", use_column_width=True, output_format='PNG')
    st.write(
        "Show your love for cricket with exclusive merchandise. From jerseys to accessories, explore a wide range "
        "of cricket-themed products. Cricket Central is your one-stop shop for cricket fan gear."
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
    
    # Make a request to the cricket API
    response = requests.get(base_url, params=params)
    
    # Process the response
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
    st.title('🏏 Live Cricket Scores: ')

    # Get live scores
    live_scores = get_live_scores()

    if live_scores:
        #st.markdown('**Live Cricket Scores:**')

        for match in live_scores:
            st.markdown(
                f"""
                <div style="
                    border: 5px solid #FFD700;
                    border-radius: 10px;
                    padding: 15px;
                    margin-bottom: 20px;
                    background-color: #000000;
                    color: #FFFFFF;
                    box-shadow: 0px 0px 10px 0px #000000;
                    animation: scale-in-center 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
                ">
                    <p style="font-size: 26px; font-weight: bold; color: #FFD700;">{match['name']}</p>
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
