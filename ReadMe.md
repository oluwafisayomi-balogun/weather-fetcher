# Weather Fetcher  

A simple Python project that fetches **real-time weather data** using the [OpenWeather API](https://home.openweathermap.org/).  

The app makes **two API calls**:  
1. **Geocoding API** – converts the city name into latitude and longitude.  
2. **Current Weather Data API** – fetches the actual weather details (temperature, wind, description) using the lat/lon.  

---

## Features  
- Input a city name and fetch current weather.  
- Handles errors gracefully (e.g., if the city isn’t found).  
- Shows weather description, temperature (°C), and wind speed/direction.  
- Uses **environment variables** (`.env`) to securely store API keys.  

---

## API  
- Weather data is provided by [OpenWeather](https://home.openweathermap.org/).  
- The free tier allows up to **1,000 API calls per day**.  

---

##  Deployment  
- Backend built with **Python (Flask)**.  
- Deployed on **Render** .

---

## Future Possible Updates  
- Add **alerts/notifications** (e.g., Telegram bot for extreme weather).  
- Suggest related locations if an incorrect location was inputted.

---