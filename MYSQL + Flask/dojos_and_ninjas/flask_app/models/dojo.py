# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for result in results:
            dojos.append(cls(result))
            # users.append( cls(use) )
        return dojos


    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES ( %(name)s, NOW(), NOW())"
        dojo_name = connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )
        return dojo_name


    @classmethod
    def ninjas_in_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s"

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        dojo_for_ninjas = cls(results[0])
        for result in results:
            data = {
                "id": result["ninjas.id"],
                "first_name": result["first_name"],
                "last_name": result["last_name"],
                "age": result["age"],
                "created_at": result["ninjas.created_at"],
                "updated_at": result["ninjas.updated_at"],
                "dojo_id": result["dojo_id"]
            }
            dojo_for_ninjas.append(Ninja(data))

        return dojo_for_ninjas

