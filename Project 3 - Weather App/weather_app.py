import requests
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'City': data['name'],
            'Temperature': f"{data['main']['temp']}°C",
            'Weather': data['weather'][0]['description'].title(),
            'Humidity': f"{data['main']['humidity']}%",
            'Wind Speed': f"{data['wind']['speed']} m/s"
        }
        return weather
    else:
        return None
def main():
    print("🌦️  Welcome to the Weather App")
    city = input("Enter city name: ")
    api_key = "927ae48dcb3724f7e71ff4eb9c159a4f"  
    result = get_weather(city, api_key)
    if result:
        print("\nWeather Details:")
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print("❌ City not found or API error.")
if __name__ == "__main__":
    main()
