from flask_app.config.mysqlconnection import connectToMySQL
from flask import session, flash

from flask_bcrypt import Bcrypt  
from flask_app import app      
bcrypt = Bcrypt(app)     
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Users:
    db = "blackbelt_db"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def save(cls,data):
        query = """INSERT INTO users ( first_name , last_name , email, password , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , %(password)s , NOW() , NOW() );"""
        return connectToMySQL(app, 'blackbelt_db').query_db( query, data )
    @staticmethod
    def validate_user(users):
        is_valid = True # we assume this is true
        if len(users['fname']) < 3:
            flash("first name must be at least 3 characters.", 'register')
            is_valid = False
        if len(users['lname']) < 3:
            flash("last name must be at least 3 characters.", 'register')
        if len(users['password']) < 8:
            flash("Password should be at least 8 characters.", 'register')
            is_valid = False
        if users['password'] != users['confirmpassword']:
            flash("passwords don't match", 'register')
            is_valid = False
        if not EMAIL_REGEX.match(users['email']): 
            flash("confirmation of password isn't correct", 'register')
            is_valid = False
        
        return is_valid
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.blackbelt_db).query_db(query)
        users = []
        for row in results:
            users.append( cls(row))
        return users
        
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])