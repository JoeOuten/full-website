from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.user import Users
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.config.mysqlconnection import connectToMySQL
# mysql = connectToMySQL(app, 'blackbelt_db')

@app.route("/")
def index():
    return render_template("index.html")
@app.route('/register', methods=['POST'])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
        "password": bcrypt.generate_password_hash(request.form['password']),
        "confirmpassword" : request.form["confirmpassword"],
    }
    if not Users.validate_user(request.form) :
        return redirect ('/')
    else:
        Users.save(data)
    session['first_name'] = request.form['fname']
    session['user_email'] = request.form['email']
    return redirect("/")
    
    

'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    user = Users.get_by_email(request.form)

    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/home')

@app.route('/shows')
def home():
    if 'user_id' not in session:
        redirect 
@app.route('/login')
def login():
    pass
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
'''
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')