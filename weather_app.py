import os
import requests
from dotenv import load_dotenv
from flask import Flask, request, render_template


# Load variables from .env
load_dotenv()
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
app = Flask(__name__)


def get_weather(location):
    try:
        geocode_url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=3&appid={OPENWEATHER_API_KEY}"
        geocode_response = requests.get(geocode_url)

        if geocode_response.status_code == 200:
            data = geocode_response.json()
            if data:
                lat, lon = data[0]["lat"], data[0]["lon"]
            else:
                return {"error": "Kindly confirm that you have the right spelling of the location.", "location": location}
        elif geocode_response.status_code == 401:
            return {"error": "Are your credentials valid?", "location": location}

        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric"
        weather_response = requests.get(weather_url)
        
        if weather_response.status_code == 200:
            data = weather_response.json()    
            main_event = data["weather"][0]["main"]
            main_event_desc = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            wind_speed = data["wind"]["speed"]
            wind_speed_kmh = round(wind_speed * 3.6, 1)
            wind_deg = data["wind"]["deg"]

            directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
            idx = round(wind_deg / 45) % 8
            wind_dir = directions[idx]

            return {
                "location": location,
                "weather": main_event,
                "description": main_event_desc, 
                "temperature_c": temp,
                "wind_speed_kmh": wind_speed_kmh,
                "wind_dir": wind_dir
            }
        else:
            return {"error": "Unable to fetch weather data.", "location": location}
    
    except Exception as e:
        return {"error": str(e), "location": location}


# Flask route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        location = request.form.get("location")
        if location:
            weather_data = get_weather(location)
            return render_template("result.html", weather=weather_data)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)




