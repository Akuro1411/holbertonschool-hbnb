from flask import Blueprint, request, jsonify
from Validation.UserValidation import create_user
from Persistance import DataManager

users = Blueprint('users', __name__)
simple_db = DataManager()


@users.route("/users")
def list_users():
    return jsonify({'User List': simple_db.data_dict['User']}), 200


@users.route("/users", methods=['POST'])
def create_new_user():
    data = request.get_json()
    new_user = create_user(firstname=data['firstName'], lastname=data['lastName'], email=data['userEmail'])
    simple_db.save(new_user)
    return jsonify({'Success': 'User is updated successfully'}), 201


@users.route("/users/<user_id>")
def get_user_id(user_id):
    user = simple_db.get(str(user_id), 'User')
    if user is None:
        return jsonify({'Error': "User is not found"}), 404

    return user, 200


@users.route("/users/<user_id>", methods=['PUT'])
def update_user_id(user_id):
    user_dict = simple_db.get(str(user_id), 'User')
    update_data = request.get_json()
    user_dict.update(update_data)  # In Python dictionaries' have update method
    updated_user = create_user(firstname=user_dict['first_name'], lastname=user_dict['last_name'],
                               email=user_dict['user_email'], password=user_dict['user_password'], is_update=True)
    updated_user.object_id = user_id
    simple_db.update(updated_user)

    return jsonify({'Success': 'User is updated successfully'}), 201


@users.route('/users/<user_id>', methods=['DELETE'])
def delete_user_id(user_id):
    user = simple_db.delete(user_id, 'User')
    if user is None:
        return jsonify({'Error': 'User is not found'}), 404
    return jsonify({'Success': 'User account is deleted'}), 204
from flask import Blueprint, request, jsonify
from Validation.UserValidation import create_user
from Persistance.DataManager import DataManager

users = Blueprint('users', __name__)
simple_db = DataManager()


@users.route("/users")
def list_users():
    return jsonify({'User List': simple_db.data_dict['User']}), 200


@users.route("/users", methods=['POST'])
def create_new_user():
    data = request.get_json()
    new_user = create_user(firstname=data['firstName'], lastname=data['lastName'], email=data['userEmail'])
    simple_db.save(new_user)
    return jsonify({'Success': 'User is updated successfully'}), 201


@users.route("/users/<user_id>")
def get_user_id(user_id):
    user = simple_db.get(str(user_id), 'User')
    if user is None:
        return jsonify({'Error': "User is not found"}), 404

    return user, 200


@users.route("/users/<user_id>", methods=['PUT'])
def update_user_id(user_id):
    user_dict = simple_db.get(str(user_id), 'User')
    update_data = request.get_json()
    user_dict.update(update_data)  # In Python dictionaries' have update method
    updated_user = create_user(firstname=user_dict['first_name'], lastname=user_dict['last_name'],
                               email=user_dict['user_email'], password=user_dict['user_password'], is_update=True)
    updated_user.object_id = user_id
    simple_db.update(updated_user)

    return jsonify({'Success': 'User is updated successfully'}), 201


@users.route('/users/<user_id>', methods=['DELETE'])
def delete_user_id(user_id):
    user = simple_db.delete(user_id, 'User')
    if user is None:
        return jsonify({'Error': 'User is not found'}), 404
    return jsonify({'Success': 'User account is deleted'}), 204
