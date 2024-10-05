
import requests

# Replace 'your_api_key' with your actual API key from OpenWeatherMap
API_KEY = 'your_api_key'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'metric' for Celsius, 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"The weather in {city} is {description} with a temperature of {temperature}°C.")
    else:
        print("City not found. Please check the city name and try again.")

def main():
    city = input("Enter the name of a city: ")
    get_weather(city)

if __name__ == "__main__":
    main()
