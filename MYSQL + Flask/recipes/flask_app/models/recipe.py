from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.time = data['time']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']
        self.id_of_recipe = None
    
    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.users_id = users.id;"
        results = connectToMySQL("recipes").query_db(query)

        recipes = []

        for row_from_db in results:
            one_recipe = cls(row_from_db)
            data = {
                "id": row_from_db["users.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "email": row_from_db["email"],
                "password": row_from_db["password"],
                "created_at": row_from_db["users.created_at"],
                "updated_at": row_from_db["users.updated_at"]
            }
            one_recipe.id_of_recipe = User(data)

            recipes.append(one_recipe) 
        return recipes

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date, time, created_at, updated_at, users_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date)s, %(time)s, NOW(), NOW(), %(users_id)s);"

        recipe_id = connectToMySQL("recipes").query_db(query,data)
        return recipe_id

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM recipes WHERE id=%(id)s;"

        results = connectToMySQL("recipes").query_db(query,data)

        one_instance = cls(results[0])
        return one_instance

    @classmethod
    def edit_recipe(cls,data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, date=%(date)s, time=%(time)s, updated_at=NOW() WHERE id=%(id)s;"

        connectToMySQL("recipes").query_db(query,data)

        return

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id= %(id)s"
        return connectToMySQL("recipes").query_db(query, data)

    @staticmethod
    def validate(data):
        is_valid = True
        if  len(data['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if  len(data['description']) < 3:
            flash("Description must be at least 3 characters.")
            is_valid = False
        if  len(data['instructions']) < 3:
            flash("Instructions must be at least 3 characters.")
            is_valid = False
        return is_valid