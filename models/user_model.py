from models.base_model import db,BaseModel
class User(BaseModel):
    __tablename__ = 'users'
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        """Modeli sözlük olarak döndürür."""
        return {
            "id": self.id,
            "name": self.username,
            "email": self.email,
        }
    @classmethod
    def add_dummy_data(cls):
        dummy_users = [
            cls(username='john_doe', email='john@example.com', password='securepassword'),
            cls(username='jane_doe', email='jane@example.com', password='anotherpassword'),
        ]
        cls.save_bulk(dummy_users)
