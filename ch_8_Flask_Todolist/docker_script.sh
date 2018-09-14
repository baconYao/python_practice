docker container run  --name db_mongo_todo_flask -v ~/Desktop/space/db:/data/db -d mongo
 
docker container run -it --name dev_flask_todo_api --link db_mongo_todo_flask:mongo -v ~/Desktop/space/python/python_practice/ch_8_Flask_Todolist/:/app -p 5000:5000  python:2.7-alpine sh