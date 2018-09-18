#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymongo

# Connect to mongodb
# "db_mongo_todo_flask" is mongodb container's name
myclient = pymongo.MongoClient("mongodb://db_mongo_todo_flask:27017/")
# Create a database called "todo_db"
todoDatabase = myclient["todo_db"]
# Create a collection called "items" in "todoDatabase"
itemCollection = todoDatabase["items"]
# Create a collection called "users" in "todoDatabase"
userCollection = todoDatabase["users"]