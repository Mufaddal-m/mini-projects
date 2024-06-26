import requests

def get_weather(api_key, city, lat, lon, part):
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        weather_description = data['current']['weather'][0]['description']
        temperature = data['current']['temp']
        humidity = data['current']['humidity']
        wind_speed = data['current']['wind_speed']
        return weather_description, temperature, humidity, wind_speed
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
    except KeyError as k:
        print(f"Invalid Response Format: {k}")
    return None

def main():
    api_key = 'bd8e31fa4c2ca97c60ff3d8d082aa5c4'  # Replace 'YOUR_API_KEY' with your actual API key
    city = input("Enter city name: ")
    lat = input("Enter latitude: ")
    lon = input("Enter longitude: ")
    part = input("Enter part to exclude (e.g., minutely, hourly, daily): ")
    weather_data = get_weather(api_key, city, lat, lon, part)
    
    if weather_data:
        weather_description, temperature, humidity, wind_speed = weather_data
        print(f"Current weather in {city}:")
        print(f"Weather: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    main()
