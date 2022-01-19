
from flask import jsonify
from model.models import ItemsModel


def findAll():
    items = ItemsModel.query.all()
    return jsonify([item.serialize for item in items])

def findOne(id):
    item = ItemsModel.query.get(id)
    if item:
        return  jsonify(item.serialize)
    
    return ({"message": "ID INVALIDO!"})

def save_new(req_data):
    new_item = ItemsModel(req_data['title'], req_data['price'], req_data['initial_quantity'], req_data['available_quantity'], req_data['sold_quantity'], req_data['condition'])
    new_item.save()

    return jsonify(new_item.serialize)