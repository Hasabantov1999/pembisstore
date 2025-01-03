# controllers/base_controller.py
import math

from flask import request, jsonify
from utils.response_wrapper import ApiResponse

class BaseController:
    def __init__(self, service):
        self.service = service

    def handle_get(self):
        """GET isteklerini işler."""
        data = self.service.get_all()
        return jsonify(ApiResponse.success(data=[item.to_dict() for item in data]))

    def handle_get_by_id(self, id):
        """ID'ye göre GET isteği."""
        data = self.service.get_by_id(id)
        if not data:
            return jsonify(ApiResponse.error(message="Data not found")), 404
        return jsonify(ApiResponse.success(data=data.to_dict()))

    def handle_create(self):
        """POST isteği ile veri oluştur."""
        data = request.get_json()
        created = self.service.create(data)
        return jsonify(ApiResponse.success(data=created.to_dict())), 201

    def handle_update(self, id):
        """PUT isteği ile veri güncelle."""
        data = request.get_json()
        updated = self.service.update(id, data)
        return jsonify(ApiResponse.success(data=updated.to_dict()))

    def handle_delete(self, id):
        """DELETE isteği ile veri sil."""
        self.service.delete(id)
        return jsonify(ApiResponse.success(message="Deleted successfully"))

    def handle_get_paginated(self):
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)

        # Sayfalama verilerini al
        pagination_data = self.service.get_paginated(page, per_page)
        total_item_count = len(self.service.get_all())  # Toplam veri sayısını al
        total_pages = math.ceil(total_item_count / per_page)  # Toplam sayfa sayısı
        # Response oluştur

        return jsonify(
            ApiResponse.success(
                data=pagination_data,
                pagination={
                    "page": page,
                    "per_page": per_page,
                    "total_item_count": total_item_count,  # Toplam veri sayısı
                    "total_pages": total_pages,  # Toplam sayfa sayısı
                    "current_items_count": len(pagination_data)  # Mevcut sayfadaki veri sayısı
                }
            )
        )