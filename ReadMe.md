# Weather Fetcher  

A simple Python project that fetches **real-time weather data** using the [OpenWeather API](https://home.openweathermap.org/).  

The app makes **two API calls**:  
1. **Geocoding API** – converts the city name into latitude and longitude.  
2. **Current Weather Data API** – fetches the actual weather details (temperature, wind, description) using the lat/lon.  

---

## Why I Built This

This project demonstrates practical API integration and backend development using Python.

It highlights my ability to:
- Work with third-party REST APIs, chaining multiple requests (geocoding → weather data).
- Design clean request/response flows and present external data in a user-friendly way.
- Include basic handling for invalid city names and API errors.
- Manage secrets securely using environment variables instead of hardcoding credentials.
- Build and deploy a lightweight Flask backend to a production environment (Render).

Beyond fetching weather data, this project reflects my approach to real-world problems: start simple, design for clarity, and leave room for future enhancements such as alerts, bots, or scheduled tasks.

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

---
