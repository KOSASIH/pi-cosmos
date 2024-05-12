from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask app
app = Flask(__name__)

# Configure the app
app.config.from_object('config')

# Initialize the database
db = SQLAlchemy(app)

# Define the Commodity model
class Commodity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

# Define the Location model
class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

# Define the Commodity service
class CommodityService:
    def __init__(self):
        self.commodities = []

    def get_all_commodities(self):
        # Return a list of commodities
        return self.commodities

    def add_commodity(self, name, description):
        # Add a new commodity
        commodity = Commodity(name=name, description=description)
        db.session.add(commodity)
        db.session.commit()
        self.commodities.append(commodity)
        return commodity

# Define the Location service
class LocationService:
    def __init__(self):
        self.locations = []

    def get_all_locations(self):
        # Return a list of locations
        return self.locations

    def add_location(self, name, address, city, state, zip_code):
        # Add a new location
        location = Location(name=name, address=address, city=city, state=state, zip_code=zip_code)
        db.session.add(location)
        db.session.commit()
        self.locations.append(location)
        return location

# Initialize the services
commodity_service = CommodityService()
location_service = LocationService()

# Define the routes
@app.route('/commodities', methods=['GET'])
def get_commodities():
    commodities = commodity_service.get_all_commodities()
    return jsonify([commodity.to_dict() for commodity in commodities])

@app.route('/commodities', methods=['POST'])
def add_commodity():
    name = request.json['name']
    description = request.json['description']
    commodity = commodity_service.add_commodity(name, description)
    return jsonify(commodity.to_dict()), 201

@app.route('/locations', methods=['GET'])
def get_locations():
    locations = location_service.get_all_locations()
    return jsonify([location.to_dict() for location in locations])

@app.route('/locations', methods=['POST'])
def add_location():
    name = request.json['name']
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']
    zip_code = request.json['zip_code']
    location = location_service.add_location(name, address, city, state, zip_code)
    return jsonify(location.to_dict()), 201

# Run the app
if __name__ == '__main__':
    if not os.path.exists('data'):
        os.makedirs('data')
    db.create_all()
    app.run(debug=True)
