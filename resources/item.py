import sqlite3

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.item import ItemModel

class Item(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank"
    )
    
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_item_by_name(name)
        if item:
            return {'item': {'name':item.name, 'price':item.price}}, 200
        return {'message':'Item not found'}, 404
        


    @jwt_required()
    def post(self, name):
        item = ItemModel.find_item_by_name(name)
        if item:
            return {'message': "An item with name '{}' already exists.".format(name)}, 400
        
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])
        item.insert()
        
        return {"message":"Inserted a new item" , "name":item.name, "price":item.price}, 201

    @jwt_required()
    def delete(self, name):
        # global items
        # items = list(filter(lambda x: x['name'] != name, items))
        item = ItemModel.find_item_by_name(name)
        if item is None:
            return {"Message":"there is no such item named {} inside the database. Delete failed!".format(name)}

        item.delete()
        return {'item': name, 'message': 'Item deleted'}
    
    @jwt_required()
    def put(self, name):
        
        data = Item.parser.parse_args()
        #new_item = {'name':name, 'price':data['price']}
        new_item = ItemModel(name, data['price'])
        # no loop version
        #item = next(filter(lambda x: x['name']==name, items), None)
        item = ItemModel.find_item_by_name(name)

        if item:
            new_item.update()
            return {'message':'Modified an existing item', 'name':new_item.name, 'price':new_item.price}
        else:
            new_item.insert()
            return {'message':'Created a new item', 'name':new_item.name, 'price':new_item.price}



class ItemList(Resource):
    @jwt_required()
    def get(self):
        
        itemlist = ItemModel.find_item_all()
        return {'items': itemlist}