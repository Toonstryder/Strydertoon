# Fully commented to show script logic

# Weather App using OpenWeatherMap API
import requests   # Imports the requests library to make HTTP requests to the API
import json       # Imports the json library (not strictly needed here since requests already returns .json())

# Step 1: API Setup
API_KEY = 'ADD_YOUR_PERSONAL_KEY_HERE'
# Your personal API key from OpenWeatherMap – required for authentication

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
# Base endpoint for current weather data in OpenWeatherMap API

# Step 2: Get Weather Data
def get_weather(city):
  """
  Fetch weather data for a given city from OpenWeatherMap API.
  Returns a dictionary with weather info if successful, otherwise None.
  """
  try:
    # Construct the full API URL with city, API key, and units in metric (Celsius)
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    # Send GET request to the API
    response = requests.get(url)

    # If request was successful (status code 200 OK)
    if response.status_code == 200:
      data = response.json()  # Convert JSON response to Python dict

      # Extract required fields into a simpler dictionary for display
      weather = {
          "City": data["name"],  # City name returned by API
          "Temperature": f"{data['main']['temp']}C",  # Current temp in Celsius
          "Weather": data["weather"][0]["description"].title(),  # Weather description (capitalized)
          "Humidity": f"{data['main']['humidity']}%",  # Humidity in %
          "Wind Speed": f"{data['wind']['speed']}m/s"  # Wind speed in meters per second
      }
      return weather  # Return the dictionary to the caller

    # If API returns 404, city not found
    elif response.status_code == 404:
      print("City not found")
      return None

    # Handle any other non-success status codes
    else:
      print("An error occurred. Status Code ", response.status_code)
      return None

  # Catch any network/other runtime exceptions
  except Exception as e:
    print(f"An error occurred: {e}")
    return None

# Step 3: Display Weather Information
def display_weather(weather):
  """
  Display the weather dictionary in a readable format.
  """
  print("\n--- Weather Information ---")
  # Loop over each key-value pair in the weather dictionary
  for key, value in weather.items():
    print(f"{key}: {value}")  # Print in 'Key: Value' format

# Step 4: Main Program Loop
while True:
  # Print main menu heading
  print("\n--- Weather App ---")

  # Ask user to enter a city name or 'q' to quit
  city = input("\nEnter a city name (or 'q' to quit): ").strip()

  # If user entered 'q' (case-insensitive), exit the loop/program
  if city.lower() == 'q':
    break

  # Fetch weather data for the entered city
  weather = get_weather(city)

  # If weather data was successfully retrieved, display it
  if weather:
    display_weather(weather)
