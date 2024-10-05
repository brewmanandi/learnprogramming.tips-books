
# Weather App

## Overview

The **Weather App** is a Python application that fetches real-time weather data for a specified city using the OpenWeatherMap API. The app uses the `requests` library to interact with the API and display the current weather conditions, including temperature and weather description.

## Features

- **Get Weather by City**: Users can input the name of a city and receive the current temperature and weather conditions for that location.
- **Error Handling**: The app handles invalid city names by displaying a helpful error message.
- **Real-Time Data**: Fetches live weather data using the OpenWeatherMap API.

## How to Run the Program

### Requirements:
- Python 3.x
- `requests` library

### Steps:
1. Install the `requests` library by running:
    ```bash
    pip install requests
    ```
2. Sign up at [OpenWeatherMap](https://openweathermap.org/api) and obtain your API key.
3. Replace `'your_api_key'` in the `weather_app.py` file with your actual API key.
4. Open a terminal or command prompt and navigate to the directory where `weather_app.py` is saved.
5. Run the program using the following command:

    ```bash
    python weather_app.py
    ```

6. Enter the name of a city when prompted, and the app will display the current weather conditions for that city.

## Example Interaction

```text
Enter the name of a city: Paris
The weather in Paris is clear sky with a temperature of 18.5°C.
```

## License

This project is open-source and available for educational purposes. Feel free to modify and share it!
