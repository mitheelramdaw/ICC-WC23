# Import necessary libraries
import streamlit as st
import requests
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor #type:ignore
from sklearn.model_selection import train_test_split #type:ignore
from sklearn.metrics import mean_squared_error #type:ignore
from PIL import Image, ImageFilter
import base64
import time

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

    # Function to add an image to the header
    image = Image.open("images/208410959-cricket-ball-and-bat-on-green-field-with-blue-sky-background.jpg")

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

    # Additional cricket-themed sections
    st.header("Cricket Highlights 🏏🌟")

    # Function to add an image to the header
    image = Image.open("images/1088609.webp")

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
    
    # Function to add an image to the header
    image = Image.open("images/fantasy.jpg")

    st.write(
        "Immerse yourself in the world of fantasy cricket. Build your dream team, score points, and compete "
        "with cricket fans worldwide. Cricket Central brings you the ultimate fantasy cricket experience."
    )

    st.header("Cricket Merchandise 🛍️")

    # Function to add an image to the header
    image = Image.open("images/merch.jpg")
    
    st.write(
        "Show your love for cricket with exclusive merchandise. From jerseys to accessories, explore a wide range "
        "of cricket-themed products. Cricket Central is your one-stop shop for cricket fan gear."
    )

# Function to load and preprocess the training data
def load_training_data():
    try:
        # Try to load data from the CSV file
        data = pd.read_csv("../Data/data.csv")
        st.write("Data loaded from data.csv.")

        # Print the first few rows of the loaded data
        st.write("First few rows of the loaded data:")
        st.write(data.head())
    except FileNotFoundError:
        # If the file is not found, fetch data from an alternative source
        st.warning("data.csv not found. Fetching data from an alternative source...")
        st.write("Data fetched from an alternative source and saved to data.csv.")
    
    # Convert categorical pitch condition to numerical values
    data['pitch_condition_numerical'] = data['pitch_condition'].map(
        {"Soft": 1, "Dry": 2, "Hard": 3, "Grass": 4}
    )

    # Convert categorical opposition strength to numerical values
    data['opposition_strength_numerical'] = data['opposition_strength'].map(
        {"Weak": 1, "Moderate": 2, "Strong": 3}
    )

   # Convert categorical weather condition to numerical values
    data['weather_condition_numerical'] = data['weather_condition'].map(
        {"Sunny": 1, "Overcast": 2, "Drizzle": 3, "Rain": 4}
    )

    return data

# Function to train the prediction model using an ensemble of RandomForest and GradientBoosting
def train_prediction_model(data):
    # Features (X) and target variable (y)
    features = ['form', 'pitch_condition_numerical', 'opposition_strength_numerical', 'weather_condition_numerical']
    X = data[features]
    y = data['performance']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Use ensemble model (RandomForest + GradientBoosting)
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    gb_model = GradientBoostingRegressor(n_estimators=100, random_state=42)

    # Fit the models
    rf_model.fit(X_train, y_train)
    gb_model.fit(X_train, y_train)

    # Make predictions on the test set
    rf_pred = rf_model.predict(X_test)
    gb_pred = gb_model.predict(X_test)

    # Ensemble predictions
    ensemble_pred = (rf_pred + gb_pred) / 2

    # Evaluate the ensemble model
    mse = mean_squared_error(y_test, ensemble_pred)
    st.write(f"Mean Squared Error on Test Set: {mse}")

    return rf_model, gb_model

def predict_performance(models, selected_form, pitch_condition, opposition_strength, weather_condition):
    # Convert pitch condition to numerical value
    pitch_condition_numerical = {'Soft': 1, 'Dry': 2, 'Hard': 3, 'Grass': 4}.get(pitch_condition, 0)

    # Convert opposition strength to numerical value
    opposition_strength_numerical = {'Weak': 1, 'Moderate': 2, 'Strong': 3}.get(opposition_strength, 0)

    # Convert weather condition to numerical value
    weather_condition_numerical = {'Sunny': 1, 'Overcast': 2, 'Drizzle': 3, 'Rain': 4}.get(weather_condition, 0)

    # Make predictions using the trained models
    rf_pred = models[0].predict([[selected_form, pitch_condition_numerical, opposition_strength_numerical, weather_condition_numerical]])
    gb_pred = models[1].predict([[selected_form, pitch_condition_numerical, opposition_strength_numerical, weather_condition_numerical]])

    # Ensemble predictions
    ensemble_pred = (rf_pred + gb_pred) / 2

    return ensemble_pred[0]


# Function to display cricket predictions
def display_cricket_predictions():
    st.title("Cricket Player Predictions 🏏")

    # Gold-themed style for titles
    st.markdown(
        """
        <style>
            .title {
                color: #FFD700;  /* Gold color for titles */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Gold-themed style for headers
    st.markdown(
        """
        <style>
            h1, h2 {
                color: #FFD700;  /* Gold color for headers */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Input for searching player information
    search_query = st.text_input("Search Player Information")

    # Weather condition selection
    st.title("Weather Conditions")
    weather_condition = st.radio("Select the weather conditions:", ["Sunny☀️", "Overcast⛅", "Drizzle🌦️", "Rain🌧️"])
    st.write(f"<span style='font-size: 18px;'>Selected weather condition: {weather_condition}</span>", unsafe_allow_html=True)

    # Slider for selecting player form
    st.title("Player Form")
    selected_form = st.slider("Select player form:", 0, 100, 50, step=10, format="%d%%")

    # Determine performance category based on selected form
    if 0 <= selected_form <= 40:
        performance_category = "Struggling 😭😭😭😭"
    elif 50 <= selected_form <= 70:
        performance_category = "Solid 😄😄😄😄😄"
    elif 80 <= selected_form <= 100:
        performance_category = "World Class 😁😁😁😁😁"
    else:
        performance_category = "Unknown"
    
    st.write(f"<span style='font-size: 18px;'>Selected form: {selected_form}%</span>", unsafe_allow_html=True)
    st.write(f"<span style='font-size: 18px;'>Player Performance Category: {performance_category}</span>", unsafe_allow_html=True)

    # Pitch condition selection
    st.title("Pitch Conditions")
    pitch_condition = st.radio("Select the pitch conditions:", ["Soft", "Dry", "Hard", "Grass"])
    st.write(f"<span style='font-size: 18px;'>The pitch condition is: {pitch_condition}</span>", unsafe_allow_html=True)

    # Opposition strength selection
    st.title("Opposition Strength")
    opposition_strength = st.radio("Select the opposition strength:", ["Weak", "Moderate", "Strong"])
    st.write(f"<span style='font-size: 18px;'>The opposition strength is: {opposition_strength}</span>", unsafe_allow_html=True)

    # Gold-themed style for the prediction button
    st.markdown(
        """
        <style>
            .prediction-button {
                background-color: #FFD700;
                color: #000000;  /* Black color for text on the button */
                font-size: 18px;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            </style>
        """,
        unsafe_allow_html=True
    )

    # Button to trigger predictions
    if st.button("Predict Performance", key="prediction_button", help="Click to get the predictions"):
        # Assuming 'models' contains the trained machine learning models
        predicted_performance = predict_performance(models, selected_form, pitch_condition, opposition_strength, weather_condition)

        # Display predicted performance in percentage form with a gold-themed style
        st.title("Predicted Performance")
        st.markdown(f"<p style='color: #FFD700; font-size: 24px;'>Predicted Performance: {predicted_performance:.2f}%</p>", unsafe_allow_html=True)


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

# Function to display the fanzone page
def show_fan_zone():
    st.header("Fan Zone")

    # Function to load a local background image
    original_image = Image.open("images/fanzone.jpg")

    # Function to add a background image to the Fan Zone section
    st.markdown(
        f"""
        <style>
            .fan-zone {{
                background-image: url('data:image/png;base64,{image_to_base64(original_image)}');
                background-size: cover;
                padding: 90px;
                color: white;
                border-radius: 10px;
                box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.3);
            }}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<div class="fan-zone">', unsafe_allow_html=True)

    # Function to create a form for users to enter their comments
    with st.form("comment_form"):
        user_comment = st.text_area("Share your thoughts")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        if not user_comment:
            st.warning("Please enter a comment before submitting.")
        else:
            add_comment(user_comment)
            st.success("Comment submitted successfully!")

    # Function to display comments from other users (replace with actual data or a database)
    st.subheader("Fan Comments")
    display_comments()

    st.markdown('</div>', unsafe_allow_html=True)

# Function for list to store comments
comments_list = []

def add_comment(comment):
    comments_list.append(comment)

def display_comments():
    # Display comments from the list
    for idx, comment in enumerate(comments_list, start=1):
        st.write(f"**Comment {idx}**: {comment}")

def image_to_base64(image):
    # Function to convert image to base64 encoding
    from io import BytesIO
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

# Main function to run the app
def main():
    
    # Sidebar navigation
    nav_option = st.sidebar.selectbox("Select Section", ["Homepage", "Cricket Predictions", "Live Cricket Scores", "Fan Zone"])

    if nav_option == "Homepage":
        display_homepage()
    elif nav_option == "Cricket Predictions":
        display_cricket_predictions()
    elif nav_option == "Live Cricket Scores":
        display_live_cricket_scores()
    elif nav_option == "Fan Zone":
        show_fan_zone()

if __name__ == "__main__":
    main()
