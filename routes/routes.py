from flask import request

import controllers.controllers as controller



def home():
    return "HOME"

def handle_all():
    if request.method == "GET":
        return controller.findAll()
    else:
        return {"message": "failure"}

def handle_find_one(id_item):
    return controller.findOne(id_item)

def handle_save():
    if request.method == "POST":
        req_data = request.get_json()
        data = controller.save_new(req_data)

        return (data, 201)
