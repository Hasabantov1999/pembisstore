from models.base_model import db

class BaseService:
    def __init__(self, model):
        self.model = model

    def get_all(self):

        return self.model.query.all()

    def get_by_id(self, item_id):

        return self.model.query.get(item_id)

    def add(self, data):

        item = self.model(**data)
        db.session.add(item)
        db.session.commit()
        return item

    def update(self, item_id, data):

        item = self.model.query.get(item_id)
        if item:
            for key, value in data.items():
                setattr(item, key, value)
            db.session.commit()
        return item

    def delete(self, item_id):

        item = self.model.query.get(item_id)
        if item:
            db.session.delete(item)
            db.session.commit()
        return item

    def get_paginated(self, page, per_page):
        query = self.model.query.paginate(page=page, per_page=per_page, error_out=False)
        return [item.to_dict() for item in query.items]