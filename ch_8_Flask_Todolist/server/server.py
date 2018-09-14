#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from flask_restplus import Api, Resource
import pymongo
import datetime
import json
from bson import json_util

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
    def get(self):
        items = itemCollection.find()        
        return [json.loads(json.dumps(item, indent=4, default=json_util.default))
                for item in items]

# # Specific item
@api.route(apiUrl + '/todo/<string:todo_id>')  
class TodoSimple(Resource):
    def get(self, todo_id):
        item = itemCollection.find_one({"_id": todo_id})
        return item, 200

    # def put(self, todo_id):
    #     # Add todo item by form-data type
    #     todos[todo_id] = request.form['data']
    #     return {todo_id: todos[todo_id]}


# Add new item
@api.route(apiUrl + '/add')
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

        return {"status": "insertion successful", "id": str(id.inserted_id)}, 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)