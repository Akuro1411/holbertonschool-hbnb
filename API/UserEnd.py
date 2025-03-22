from flask import Blueprint, request
from Model.Users import User
from Persistance.DataManager import DataManager

users = Blueprint('users', __name__)
simple_db = DataManager()


@users.route("/users")
def list_users():
    return {'User List': simple_db.data_dict['User']}


@users.route("/users", methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(firstname=data['firstname'], user_mail=data['email'], lastname=data['lastname'])
    simple_db.save(new_user)
    return 'User is created successfully'


@users.route("/users/<user_id>")
def get_user_id(user_id):
    return simple_db.get(str(user_id), 'User')


@users.route("/users/<user_id>", methods=['PUT'])
def update_user_id(user_id):
    user_dict = simple_db.get(str(user_id), 'User')
    user_dict['user_password'] = request.form['user_password']
    return 'User is updated successfully'


@users.route('/users/<user_id>', methods=['DELETE'])
def delete_user_id(user_id):
    simple_db.delete(user_id, 'User')
    return 'User account is deleted'
