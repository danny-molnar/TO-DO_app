from flask import Flask, request, Response, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config
import json


app = Flask(__name__, instance_relative_config=False)
app.config.from_object(Config)
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column(db.VARCHAR(length=100))
    complete = db.Column(db.Boolean)


@app.route("/")
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    #db.create_all()
    app.run(debug=True)