from flask import request, jsonify
from functools import wraps
from utils.rules import rules
from utils.response_wrapper import ApiResponse


def requires_permission(permission):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # JWT'den role bilgisini al
            token_data = request.headers.get("Authorization")
            if not token_data:
                return ApiResponse.unauthorized()

            user_role = token_data.get("role")

            # Role göre yetki kontrolü
            if user_role not in rules or permission not in rules[user_role]:
                return ApiResponse.forbidden()

            return func(*args, **kwargs)
        return wrapper
    return decorator