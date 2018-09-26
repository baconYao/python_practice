from flask import request, jsonify
from bson import json_util
from bson.objectid import ObjectId
from flask_restplus import Resource
import handler
import json
import datetime
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
import sys
sys.path.insert(0, './../')
from db_connection import userCollection


class Users(Resource):
    # Get all users' information
    def get(self):
        users = userCollection.find()
        if users is not None:
            returnObject = {
                "ok": True,
                "message": "get all users",
                "users": handler.handle_encode(self, users)
            }
            return returnObject
        return None, 204

    # Delete all users
    def delete(self):
        try:
            userCollection.delete_many({})
            return {'ok': True, 'message': 'Users deleted'}, 200
        except Exception, error:
            # print "Unexpected error:", error
            return {"ok": False, "message": error}, 400

class Signup(Resource):
    def post(self):
        # get one user's information 
        data = request.get_json()
        # Create empty list and store information into it
        user_list = {}
        user_list['account'] = data['account']
        user_list['password'] = data['password']
        user_list['repassword'] = data['repassword']
        user_list['joinedDate'] = str(datetime.datetime.now())

        # check password and repassword
        if user_list['password'] != user_list['repassword']:
            return {"message": "Passwrod and repassword are different"}, 400

        # check user whether exist or not
        cu = userCollection.find({"account": user_list['account']})
        for x in cu:
            print x
            if x :
                return {"message": "Account exist or wrong password "}, 400
        # Insert list (one document) into db
        id = userCollection.insert_one(user_list)
        return {"ok": True, "message": "Singup successful", "id": str(id.inserted_id), "user": handler.handle_encode(self, user_list)}, 201

class Login(Resource):
    def post(self):
        # get one user's information 
        data = request.get_json()
        # Create empty list and store information into it
        user_list = {}
        user_list['account'] = data['account']
        user_list['password'] = data['password']

        user = userCollection.find_one({"account": user_list['account']})

        if user is None or user["password"] != user_list['password']:
            return {"message": "Failed login"}, 401
        
        # Add user's OID into token
        access_token = create_access_token(identity = str(user["_id"]))
        print access_token

        return {"token": access_token}, 200

