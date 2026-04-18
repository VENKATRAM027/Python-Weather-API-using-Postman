import os
from flask import Flask
from dotenv import load_dotenv
from api.routes import weather_api

# Load environment variables from the .env file
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

# Register the routes we defined in api/routes.py
app.register_blueprint(weather_api)

if __name__ == '__main__':
    # Grab the port from the .env file, default to 5000 if not found
    port = int(os.getenv("PORT", 5000))
    
    # Run the server
    app.run(debug=True, host='127.0.0.1', port=port)