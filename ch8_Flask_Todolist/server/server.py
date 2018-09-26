#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_restplus import Api, Resource
from flask_jwt_extended import JWTManager
import sys

app = Flask(__name__)
# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

api = Api(app, version='1.0', title='TodoMVC API', description='A simple TodoMVC API')

sys.path.insert(0, './controller')
import users_controller as uc
import items_controller as ic

apiUrl = '/api'
todoUrl = '/todo'
userUrl = '/user'

api.add_resource(ic.GetAllItems, apiUrl + todoUrl)
api.add_resource(ic.GetOneItem, apiUrl + todoUrl + '/<string:todo_id>')
api.add_resource(ic.AddItem, apiUrl + todoUrl + '/add')
api.add_resource(uc.Users, apiUrl + userUrl)
api.add_resource(uc.Signup, apiUrl + userUrl + '/signup')
api.add_resource(uc.Login, apiUrl + userUrl + '/login')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)