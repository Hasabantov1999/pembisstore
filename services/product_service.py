# services/product_service.py
from services.base_service import BaseService
from models.product_model import Product

class ProductService(BaseService):
    def __init__(self):
        super().__init__(Product)