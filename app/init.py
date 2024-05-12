# Initialize the Flask app
from flask import Flask
app = Flask(__name__)

# Import routes and services
from .routes import commodity_routes, location_routes
from .services import commodity_service, location_service
