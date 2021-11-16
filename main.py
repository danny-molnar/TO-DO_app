# Creating first REST API with Flask
from flask import Flask, request, Response, render_template
import json
from datetime import date
import calendar

app = Flask(__name__)

# the database will be a JSON, like below
# setting up a dummy JSON with some basic data in it

# task:
## short_desc
## long_desc
## date_created
## date_due
## done

today = date.today()
today_name = calendar.day_name[today.weekday()]

tasks_db = {
    "1" : {
        "short_desc" : "Make Coffee", 
        "long_desc" : "Make Coffee, use new beans",
        "date_created" : "12. 11. 2021.",
        "date_due" : "13. 11. 2021.",
        "done" : "No" 
    },
    "2" : {
        "short_desc" : "Tidy up", 
        "long_desc" : "Tidy up the living room, do some cleaning",
        "date_created" : "12. 11. 2021.",
        "date_due" : "14. 11. 2021.",
        "done" : "No" 
    }
}

@app.route("/")
def hello():
    #html_response = "Good morning! Welcome to your TODO list!<br>"
    #html_response += "Today is " + str(today) + ", " + str(today_name) + "."
    return render_template("home.html")
    #return html_response 

@app.route("/about")
def about():
    #html_response = "Good morning! Welcome to your TODO list!<br>"
    #html_response += "Today is " + str(today) + ", " + str(today_name) + "."
    return render_template("about.html")
    #return html_response 

@app.route("/tasks")
def tasks():
    """ html_response = "<ul>"
    for t in tasks_db:
        html_response += "<li>" + tasks_db[t]["short_desc"] + "</li>"
    html_response += "</ul>"
    return html_response """
    
    # Here we need to link the tasks to the output html
    
    

# READ, and search for movie data by id
@app.route("/tasks/<task_id>")
def get_task(task_id):
    return json.dumps(tasks_db[task_id])
    #perhaps add a html_response string and concat the deets to that string and return 


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