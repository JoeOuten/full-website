from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.show import show
from flask_app.models.user import Users
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.config.mysqlconnection import connectToMySQL

@app.route('/shows')
def home():
    return render_template("show.html")

@app.route('/shows/')
def view():
    return render_template("office.html")
@app.route('/shows/edit')
def edit():
    return render_template("edit.html")
@app.route('/shows/delete')
def delete():
    return redirect("/")
@app.route('/shows/new')
def new():
    return render_template('add.html')
@app.route('/shows/cre', methods=['POST'])
def add():
    data = {
        "title": request.form["title"],
        "network" : request.form["network"],
        "description" : request.form["description"],
    }
    return show.add_show(data)
