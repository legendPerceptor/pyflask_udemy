import sqlite3
from db import db

class ItemModel(db.Model):
    DATAFILE = 'data.db'
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {"store_id":self.store_id, "name":self.name, "price":self.price}

    @classmethod
    def find_item_by_name(cls, name):
        return ItemModel.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name

    @classmethod
    def find_item_all(cls):
        items = ItemModel.query.all()
        itemlist = [item.json() for item in items]
        return itemlist

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        # no return value

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        # no return value
