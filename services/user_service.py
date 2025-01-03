# services/user_service.py
from services.base_service import BaseService
from models.user_model import User

class UserService(BaseService):
    def __init__(self):
        super().__init__(User)