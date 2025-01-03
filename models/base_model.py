from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @classmethod
    def add_dummy_data(cls):
        raise NotImplementedError("Bu metot model sınıfında override edilmelidir.")

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def save_bulk(objects):
        if objects:
            db.session.bulk_save_objects(objects)
            db.session.commit()
            print(f"{len(objects)} obje başarıyla kaydedildi.")
        else:
            print("Kaydedilecek obje yok.")
