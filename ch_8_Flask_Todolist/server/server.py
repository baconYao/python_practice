from flask import Flask, request
from flask_restplus import Api, Resource
app = Flask(__name__)
api = Api(app, version='1.0', title='TodoMVC API', description='A simple TodoMVC API')

todos = {}

@api.route('/')
class Hello(Resource):
    def get(self):
        return {"hello": "world"}

@api.route('/<string:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)