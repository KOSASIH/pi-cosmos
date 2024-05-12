# Define routes for commodities
from flask import Blueprint, request, jsonify
from .services import commodity_service

commodity_bp = Blueprint('commodity', __name__)

@commodity_bp.route('/commodities', methods=['GET'])
def get_commodities():
    commodities = commodity_service.get_all_commodities()
    return jsonify([commodity.to_dict() for commodity in commodities])
