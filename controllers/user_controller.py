# controllers/user_controller.py

from services.user_service import UserService
from controllers.base_controller import BaseController
# from utils.permissions import requires_permission


class UserController(BaseController):
    def __init__(self):
        super().__init__(UserService())

    # @requires_role("view_users")
    def handle_get_paginated(self):
        return super().handle_get_paginated()


