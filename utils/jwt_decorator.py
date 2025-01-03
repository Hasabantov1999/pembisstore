from flask import request
from functools import wraps
import jwt
from utils.response_wrapper import ApiResponse

SECRET_KEY = "your_secret_key"  # JWT için kullanılan gizli anahtar

def jwt_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return ApiResponse.forbidden(
                message="Unauthorized",
                description="Token is missing or invalid."
            ), 401

        try:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            request.user = decoded_token  # Kullanıcı bilgilerini request'e ekle
        except jwt.ExpiredSignatureError:
            return ApiResponse.forbidden(
                message="Unauthorized",
                description="Token has expired."
            ), 401
        except jwt.InvalidTokenError:
            return ApiResponse.forbidden(
                message="Unauthorized",
                description="Invalid token."
            ), 401

        return func(*args, **kwargs)
    return wrapper