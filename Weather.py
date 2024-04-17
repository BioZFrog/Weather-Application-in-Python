import requests
import time

print("--------___------------------Weather Application in Python------------------___--------")

# Starting Format & OpenWeatherMap API 
try:
    API_KEY = " " # Active OpenWeatherMap API Key
    CITY = input("\nEnter a City name: ")
    BASE_URL = f"https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={CITY}" # OpenWeatherMap URL

    # Forecast details
    response = requests.get(BASE_URL).json()

    weather = response['weather'][0]['main']
    weather_description = response['weather'][0]['description']

    temp_kelvin = response['main']['temp']
    
    temp_celcius = temp_kelvin - 273.15
    temp_celcius = round(temp_celcius)
    
    temp_fahrenheit = (temp_celcius * 9/5) + 32
    temp_fahrenheit = round(temp_fahrenheit)
    
    humidty = response['main']['humidity']
    wind = response['wind']['speed']
    
    country = response['sys']['country']

# Forecast Generation & Formating
    print("Generating Forecast in Terminal....")
    time.sleep(3)
    print(f"\nThe Weather forecast is Ready!. The weather in {CITY}, {country} is {weather}, or in detail its {weather_description}. Furthermore, the detected Temperature is {temp_celcius}°C, {temp_kelvin}K, and {temp_fahrenheit}°F with the Humidity level of {humidty}% and Wind speed of {wind}\n")
except:
    print("There was a problem detected. Please enter Valid Data")
