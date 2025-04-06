from flask import Blueprint, request, jsonify
from Persistance import simple_db
from Model.Amenities import Amenity
amenities = Blueprint("amenities", __name__)


@amenities.route('/amenities', methods=['GET', 'POST'])
def get_post_amenities():
    total_amenities = simple_db.data_dict['Amenity']
    amenity_list = []
    for amenity_id in total_amenities:
        amenity_list.append({total_amenities[amenity_id]["amenity_name"]: amenity_id})

    if request.method == 'GET':
            return jsonify({"Amenity list": amenity_list}), 200

    if request.method == 'POST':
        try:
            data = request.get_json()
            amenities_name = [list(name)[0] for name in amenity_list]
            if data['amenityName'] and data['amenityName'] not in amenities_name:
                new_amenity = Amenity(name=data['amenityName'])
                simple_db.save(new_amenity)
                return jsonify({"Success": "New amenity is created",
                                "Amenity id": new_amenity.object_id}), 201
            else:
                return jsonify({"Error": "Amenity exists in list"}), 409
        except Exception:
            return jsonify({"Error": "Post data is not valid"}), 400


@amenities.route('/amenities/<amenity_id>', methods=['GET', 'PUT', 'DELETE'])
def work_with_id(amenity_id):
    total_amenities = simple_db.data_dict['Amenity']
    if request.method == 'GET':
        try:
            return jsonify(total_amenities[amenity_id])
        except Exception:
            return jsonify({"Error": "There is no such amenity"}), 409
    elif request.method == 'PUT':
        try:
            data = request.get_json()
            amenity = total_amenities[amenity_id]
            amenity.update(data)
            return jsonify({"Success": "Amenity is updated successfully"}), 201
        except Exception:
            return jsonify({"Error": "Put data is not valid"}), 400
    elif request.method == 'DELETE':
        try:
            simple_db.delete(entity_id=amenity_id, entity_type='Amenity')
            return jsonify({"Success": "Amenity is deleted successful"}), 204
        except Exception:
            return jsonify({"Error": "There is no such amenity"}), 409

