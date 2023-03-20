from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comments = data['comments']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all( cls):
        query = "SELECT * FROM dojo ORDER BY dojo.id DESC LIMIT 1;"
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        return Dojo(results[0])

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojo ( name , location , language , comments, created_at , updated_at ) VALUES ( %(name)s , %(location)s , %(language)s , %(comments)s, NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        user_id = connectToMySQL('dojo_survey_schema').query_db( query, data )
        return user_id


    @staticmethod
    def validate_user(dojo):
        is_valid = True # we assume this is true
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if (len(dojo['location']) == 21):
            flash("Must select a location")
            is_valid = False
        if (len(dojo['language']) == 21):
            flash("Must select a language")
            is_valid = False
        if len(dojo['comments']) < 3:
            flash("Comments must be at least 3 characters.")
            is_valid = False
        return is_valid