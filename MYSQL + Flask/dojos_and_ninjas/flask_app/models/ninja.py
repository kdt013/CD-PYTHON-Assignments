# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        # Create an empty list to append our instances of friends
        ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        for result in results:
            one_instance = cls(result)
            ninjas.append(one_instance)

        return ninjas

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (first_name, last_name, age created_at, updated_at, dojo_id) VALUES ( %(first_name)s, %(last_name)s, %(age)s,  NOW(), NOW(), %(dojo_id)s)"
        dojo_name = connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )
        return dojo_name