from flask import session, flash
from flask_app.config.mysqlconnection import connectToMySQL

from flask_bcrypt import Bcrypt  
from flask_app import app      
bcrypt = Bcrypt(app)     
import re
release_date_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class show:
    db = "blackbelt_db"

    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.actions = data['actions']
        self.likes = data['likes']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def add_show(cls,data):
        query = """INSERT INTO shows ( title , network , release_date, description , created_at, updated_at ) VALUES ( %(title)s , %(network)s , %(release_data)s , %(description)s , NOW() , NOW() );"""
        return connectToMySQL(app, 'blackbelt_db').query_db( query, data )
  