from flask import Blueprint, request, jsonify
from services.weather_fetch import fetch_weather_for_city

# 1. Create a Modular App
weather_api = Blueprint('weather_api', __name__)

# 2. Define the Entry Point
@weather_api.route('/api/weather', methods=['GET'])
def get_weather():
    
    # 3. Check User Input
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "Please provide a city name."}), 400

    # 4. Delegate to the Brain
    weather_data = fetch_weather_for_city(city)

    # 5. Format the Final Response
    if weather_data:
        return jsonify({
            "city": city.title(),
            "weather": weather_data
        }), 200
    else:
        return jsonify({"error": f"Weather data for '{city}' not found."}), 404