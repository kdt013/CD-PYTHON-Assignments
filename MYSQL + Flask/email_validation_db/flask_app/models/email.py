import re
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO email ( email , created_at, updated_at ) VALUES ( %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        email_id = connectToMySQL('email').query_db( query, data )  

        return email_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM email;"

        results = connectToMySQL('email').query_db(query)
        # Create an empty list to append our instances of friends
        email = []
        # Iterate over the db results and create instances of friends with cls.
        for result in results:
            one_instance = cls(result)
            email.append(one_instance)
            # users.append( cls(use) )
        return email

    @staticmethod
    def validate_email(email):
        is_valid = True # we assume this is true
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid
