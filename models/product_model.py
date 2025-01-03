from models.base_model import db,BaseModel
class Product(BaseModel):
    __tablename__ = 'products'
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)


    @classmethod
    def add_dummy_data(cls):
        dummy_products = [
            cls(name='Laptop', price=999.99, stock=10),
            cls(name='Smartphone', price=499.99, stock=50),
        ]
        cls.save_bulk(dummy_products)