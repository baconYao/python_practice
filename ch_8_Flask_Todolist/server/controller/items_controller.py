from flask import request
from bson import json_util
from bson.objectid import ObjectId
from flask_restplus import Resource
import handler
import json
import datetime
from flask_jwt_extended import get_jwt_identity, jwt_required
import sys
sys.path.insert(0, './../')
from db_connection import itemCollection


class GetAllItems(Resource):
    # Get all items
    def get(self):
        items = itemCollection.find()
        if items is not None:
            returnObject = {
                "ok": True,
                "message": "get all records",
                "items": handler.handle_encode(self, items)
            }
            return returnObject
        return None, 204
    
    # Delete all items
    def delete(self):
        try:
            itemCollection.delete_many({})
            return {'ok': True, 'message': 'Records deleted'}, 200
        except Exception, error:
            # print "Unexpected error:", error
            return {"ok": False, "message": error}, 400

class GetOneItem(Resource):
    # Retrieve specific data of the item
    @jwt_required
    def get(self, todo_id):
        current_user = get_jwt_identity()
        # print
        # print current_user
        # print
        try:
            item = itemCollection.find_one({"_id": ObjectId(todo_id)})
            returnObject = {
                "ok": True,
                "message": "get specific record",
                "items": handler.handle_encode(self, item)
            }
            if item is not None:
                return returnObject
            return None, 204
        except Exception, error:
            # print "Unexpected error:", error
            return {"ok": False, "message": error}, 400

    # Update specific data of the item
    def put(self, todo_id):
        # Add todo item by form-data type
        name = request.form['Name']
        description = request.form['Description']

        try:
            itemCollection.update_one(
                {
                    "_id": ObjectId(todo_id)
                },
                {
                    "$set": {
                        "Name": name,
                        "Description": description
                    }
                }
            )
            return {"ok": True, "message": "update successful", "id": todo_id}, 202
        except Exception, error:
            # print "Unexpected error:", error
            return {"ok": False, "message": error}, 400

    # Delete specific data of the item
    def delete(self, todo_id):
        try:
            c = itemCollection.delete_one({"_id": ObjectId(todo_id)})
            return {'ok': True, 'message': 'Record deleted'}, 200
        except Exception, error:
            # print "Unexpected error:", error
            return {"ok": False, "message": error}, 400

class AddItem(Resource):
    def post(self):
        # get one item's value 
        data = request.get_json()
        # Create empty list and store data into it
        todos_list = {}
        todos_list['Name'] = data['Name']
        todos_list['Description'] = data['Description']
        todos_list['CreatedDate'] = str(datetime.datetime.now())
        # print todos_list
        # Insert list (one document) into db
        id = itemCollection.insert_one(todos_list)

        return {"ok": True, "message": "insertion successful", "id": str(id.inserted_id)}, 201