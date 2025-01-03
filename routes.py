# routes.py

from flask import Blueprint
from controllers.user_controller import UserController

api = Blueprint('api', __name__)


# users
user_controller = UserController()

api.add_url_rule('/users', 'get_users', user_controller.handle_get_paginated, methods=['GET'])
api.add_url_rule('/users/<int:id>', 'get_user_by_id', user_controller.handle_get_by_id, methods=['GET'])
api.add_url_rule('/users', 'create_user', user_controller.handle_create, methods=['POST'])
api.add_url_rule('/users/<int:id>', 'update_user', user_controller.handle_update, methods=['PUT'])
api.add_url_rule('/users/<int:id>', 'delete_user', user_controller.handle_delete, methods=['DELETE'])