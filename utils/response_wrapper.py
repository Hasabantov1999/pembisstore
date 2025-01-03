# utils/response_wrapper.py
from utils.config import Config
from utils.lang_helper import get_translation


class ApiResponse:
    @staticmethod
    def success(data=None, message=None, description=None, status=200, code=None, pagination=None):
        """Başarılı yanıt için standart format."""
        return {
            "data": data or {},
            "status": status,
            "code": code,
            "message": message,
            "description": description,
            "version": Config.VERSION,
            "pagination": pagination,
        }

    @staticmethod
    def error(message="Error", description=None, status=400, code=None):
        """Hata yanıtı için standart format."""
        return {
            "data": None,
            "status": status,
            "code": code,
            "message": message,
            "description": description,
            "version": Config.VERSION,
            "pagination": None,
        }

    @staticmethod
    def forbidden(language="tr"):
        """Yetkisiz erişim için standart hata formatı."""
        message = get_translation("forbidden_access", language)
        description = get_translation("forbidden_description", language)
        return {
            "data": None,
            "status": 403,
            "code": "FORBIDDEN",
            "message": message,
            "description": description,
            "version": Config.VERSION,
            "pagination": None,
        }

    @staticmethod
    def notfound(key="not_found", language="tr"):
        """Veri bulunamadı hatası."""
        message = get_translation(key, language)
        description = get_translation(key, language)
        return {
            "data": None,
            "status": 404,
            "code": "NOT_FOUND",
            "message": message,
            "description": description,
            "version": Config.VERSION,
            "pagination": None,
        }

    @staticmethod
    def unauthorized(language="tr"):
        message = get_translation("unauthorized_access", language)
        description = get_translation("unauthorized_description", language)
        return {
            "data": None,
            "status": 401,
            "code": "UNAUTHORIZED",
            "message": message,
            "description": description,
            "version": Config.VERSION,
            "pagination": None,
        }