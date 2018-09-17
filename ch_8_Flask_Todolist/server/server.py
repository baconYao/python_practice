#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from flask import Flask, request, jsonify
from flask_restplus import Api, Resource
import pymongo
import datetime
import json
from bson import json_util
from bson.objectid import ObjectId
import handler

# Connect to mongodb
# "db_mongo_todo_flask" is mongodb container's name
myclient = pymongo.MongoClient("mongodb://db_mongo_todo_flask:27017/")
# Create a database called "todo_db"
todoDatabase = myclient["todo_db"]
# Create a collection called "items" in "todoDatabase"
itemCollection = todoDatabase["items"]

app = Flask(__name__)
api = Api(app, version='1.0', title='TodoMVC API', description='A simple TodoMVC API')

# Item Schema
"""
    _id: Mongodb generates it automatically
    Name: Item's name
    Description: Item's detail data
    CreatedDate: When is the item be created
"""

apiUrl = '/api'

@api.route(apiUrl + '/todo')
class GetAllItems(Resource):
    # Get all items
    def get(self):
        items = itemCollection.find()
        if items is not None:
            returnObject = {
                "ok": True,
                "message": "get all records",
                "items": handler.handle_encode(self, items, True)
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

# Specific item
@api.route(apiUrl + '/todo/<string:todo_id>')  
class TodoSimple(Resource):
    # Retrieve specific data of the item
    def get(self, todo_id):
        try:
            item = itemCollection.find_one({"_id": ObjectId(todo_id)})
            returnObject = {
                "ok": True,
                "message": "get specific record",
                "items": handler.handle_encode(self, item, False)
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
            itemCollection.delete_one({"_id": ObjectId(todo_id)})
            return {'ok': True, 'message': 'Record deleted'}, 200
        except Exception, error:
            # print "Unexpected error:", error
            return {"ok": False, "message": error}, 400

# Add new item
@api.route(apiUrl + '/add/todo')
class AddItem(Resource):
    def post(self):
        # get one item's value 
        data = request.get_json()
        # Create empty list and store data into it
        todos_list = {}
        todos_list['Name'] = data['Name']
        todos_list['Description'] = data['Description']
        todos_list['CreatedDate'] = str(datetime.datetime.now())
        print todos_list
        # Insert list (one document) into db
        id = itemCollection.insert_one(todos_list)

        return {"ok": True, "message": "insertion successful", "id": str(id.inserted_id)}, 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)