# Creating first REST API with Flask
from flask import Flask, request, Response
import json

app = Flask(__name__)

# the database will be a JSON, like below
movie_db = {
    "1" : {"name" : "Stargate", "release_date" : "1994"},
    "2" : {"name" : "Sunshine", "release_date" : "2007"}
}

@app.route("/")
def hello():
    return "Hello world!<a href=/movies> Click here for the movie database! </a>"

@app.route("/movies")
def movies():
    return json.dumps(movie_db)

# READ, and search for movie data by id
@app.route("/movie/<movie_id>")
def get_movie(movie_id):
    return json.dumps(movie_db[movie_id])


# route for Creating a new item with POST, notice the methods argument which is a list of methods
@app.route("/movie/add", methods=['POST'])
def add_movie():
    req_data = request.get_json() 
    movie = req_data['movie']
    
    new_movie = {"4" : movie}
    movie_db.update(new_movie)
    
    return "Movie added"


##new movie to be added
# { "movie" : { "name" : "The Matrix", "release_date" : "1999" } }


if __name__ == "__main__":
    app.run(host="127.0.0.1")
    
# CRUD: Create, Read, Update, Delete api calls as HTTP requests
# CREATE - POST
# READ   - GET
# UPDATE - PUT
# DELETE - GET

# my app: To-do list. Team: Tyrone, Esther, Gareth, Chris, Danny
 
# Functionalities of the app:
# - add tasks
# - tick tasks, but still visible
# - delete tasks
 
# UI:
# - empty list on launch or load saved list, maybe in a JSON 
# - 