from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @staticmethod
    def validate(data):
        is_valid = True

        if data["password"] != data["confirm_password"]:
            flash("Passwords do not match!")
            is_valid = False

        return is_valid

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"

        user_id = connectToMySQL("belt_review_sept2022").query_db(query,data)

        return user_id

    @classmethod
    def find_one_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"

        results = connectToMySQL("belt_review_sept2022").query_db(query,data)

        if len(results) == 0:
            return False
        
        one_instance = cls(results[0])
        return one_instance

    @classmethod
    def find_one_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"

        results = connectToMySQL("belt_review_sept2022").query_db(query,data)

        if len(results) == 0:
            return False
        
        one_instance = cls(results[0])
        return one_instance
    
