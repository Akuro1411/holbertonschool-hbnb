from flask import Blueprint, request, jsonify
from Persistance.DataManager import simple_db
from Model.Reviews import Review

reviews = Blueprint("reviews", __name__)


@reviews.route('/places/<place_id>/reviews', methods=['GET', 'POST'])
def reviews_and_places(place_id):
    if request.method == 'GET':
        try:
            keys = simple_db.data_dict['Review'].keys()
            all_reviews = simple_db.data_dict['Review']
            reviews_for_place = []
            for key in keys:
                if all_reviews[key]['place_id'] and all_reviews[key]['place_id'] == place_id:
                    reviews_for_place.append(all_reviews[key])
            return jsonify(reviews_for_place)
        except Exception:
            return jsonify({"Error": "Entered place doesn't exist"})
    if request.method == 'POST':
        try:
            data = request.get_json()
            place = simple_db.get(place_id, 'Place')
            user = simple_db.get(data['userId'], 'User')
            if data:
                if place and user:
                    new_review = Review(user=data['userId'], place=str(place_id), rate=data['placeRate'], comment=data['userComment'])
                    place['reviews'].append(new_review.object_id)
                    simple_db.save(new_review)
                    return jsonify({"Success": "Your review is added"})
                else:
                    return jsonify({"Error": "This place doesn't exist"})
        except Exception:
            return jsonify({"Error": "Missing fields at review"}), 400
    return None


@reviews.route("/reviews/<review_id>", methods=['GET', 'PUT', 'DELETE'])
def work_on_review(review_id):
    if request.method == 'GET':
        try:
            review = simple_db.get(review_id, "Review")
            return review
        except Exception:
            return jsonify({"Error": "Review id's field is empty"})

    if request.method == 'PUT':
        try:
            data = request.get_json()
            if data:
                review = simple_db.get(review_id, "Review")
                review.update(data)
                return jsonify({"Success": "The review is updated successfully"})
            else:
                return jsonify({"Error": "There is no data for update process"})
        except Exception:
            return jsonify({"Error": "Entered review doesn't exist"})

    if request.method == 'DELETE':
        try:
            simple_db.delete(review_id, "Review")
            return jsonify({"Success": "Review is deleted successfully"})
        except Exception:
            return jsonify({"Error": "There is no such review"})
    return 0

