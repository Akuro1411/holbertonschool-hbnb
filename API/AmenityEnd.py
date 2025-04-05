from flask import Blueprint, request, jsonify
from Persistance import simple_db

amenities = Blueprint("amenities", __name__)


@amenities.route('/amenities')
def get_amenities():
    return jsonify({"Amenity list": simple_db.data_dict['Amenity']}), 200


from flask import Blueprint, request, jsonify
from Persistance import simple_db

amenities = Blueprint("amenities", __name__)


@amenities.route('/amenities')
def get_amenities():
    return jsonify({"Amenity list": simple_db.data_dict['Amenity']}), 200

