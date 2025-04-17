from flask import Blueprint, request, jsonify
from Model.Places import Place
from Persistance.DataManager import simple_db

places = Blueprint('Places', __name__)


@places.route('/places', methods=['GET', 'POST'])
def get_or_create_place():
    total_places = simple_db.data_dict['Place']
    list_places = []
    for place_id in total_places:
        list_places.append({total_places[place_id]['name']: place_id})
    if request.method == 'GET':
        return jsonify(list_places), 200

    if request.method == 'POST':
        data = request.get_json()
        try:
            all_places = simple_db.data_dict['Place']
            coordinates = [(all_places[obj_id]["latitude"], all_places[obj_id]["longitude"]) for obj_id in all_places]
            if (data['placeLati'], data['placeLong']) not in coordinates:
                new_place = Place(place_name=data['placeName'],
                                  place_price=data['placePrice'],
                                  place_address=data['placeAddress'],
                                  place_bathroom=data['placeBathroom'],
                                  place_latitude=data['placeLati'],
                                  place_longitude=data['placeLong'],
                                  place_description=data['placeDesc'],
                                  guest_number=data['guestNumber'],
                                  count_rooms=data['countRooms'])
                simple_db.save(new_place)
                return jsonify({"Success": "The new place is added successfully"}), 201
            else:
                return jsonify({"Error": "The place exists at given coordinates"}), 409
        except Exception:
            return jsonify({"Error": "Post data is not valid"}), 400


@places.route('/places/<place_id>', methods=['GET', 'PUT', 'DELETE'])
def work_with_id(place_id):
    if request.method == 'GET':
        try:
            data = simple_db.get(place_id, "Place")
            return jsonify(data), 200
        except Exception:
            return jsonify({"Error": "There is no such place"})

    if request.method == 'PUT':
        try:
            data = request.get_json()
            place = simple_db.get(place_id, "Place")
            place.update(data)
            return jsonify({"Success": "Place is updated successfully"}), 201
        except Exception:
            return jsonify({"Error": "Put data is not valid"})

    if request.method == 'DELETE':
        try:
            simple_db.delete(place_id, "Place")
            return jsonify({"Succes": "Place is deleted"}), 204
        except Exception:
            return jsonify({"Error": "There is no such place"})

