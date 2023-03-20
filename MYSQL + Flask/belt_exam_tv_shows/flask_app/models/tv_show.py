from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class TV_Show:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']
        self.id_of_show = None

    
    @classmethod
    def get_all_tv_shows(cls):
        query = "SELECT * FROM tv_shows JOIN users ON tv_shows.users_id = users.id;"
        results = connectToMySQL("tv_shows").query_db(query)

        tv_shows= []

        for row_from_db in results:
            one_show = cls(row_from_db)
            data = {
                "id": row_from_db["users.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "email": row_from_db["email"],
                "password": row_from_db["password"],
                "created_at": row_from_db["users.created_at"],
                "updated_at": row_from_db["users.updated_at"]
            }
            one_show.id_of_show = User(data)

            tv_shows.append(one_show)
        return tv_shows

    @classmethod
    def save(cls,data):
        query = "INSERT INTO tv_shows (title, network, release_date, description, created_at, updated_at, users_id) VALUES (%(title)s, %(network)s, %(release_date)s, %(description)s, NOW(), NOW(), %(users_id)s);"

        tv_show_id = connectToMySQL("tv_shows").query_db(query,data)

        return tv_show_id

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM tv_shows WHERE id=%(id)s;"

        results = connectToMySQL("tv_shows").query_db(query,data)

        one_instance = cls(results[0])
        return one_instance

    @classmethod
    def edit_show(cls,data):
        query = "UPDATE tv_shows SET title=%(title)s, network=%(network)s, release_date=%(release_date)s, description=%(description)s, updated_at=NOW() WHERE users_id=%(users_id)s;"

        connectToMySQL("tv_shows").query_db(query,data)
        return

    @classmethod
    def delete_show(cls, data):
        query = "DELETE FROM tv_shows WHERE id=%(id)s"
        return connectToMySQL("tv_shows").query_db(query, data)



    @staticmethod
    def validate(data):
        is_valid = True
        if  len(data['title']) < 3:
            flash("Title must be at least 3 characters.")
            is_valid = False
        if  len(data['network']) < 3:
            flash("Network must be at least 3 characters.")
            is_valid = False
        if  len(data['release_date']) == 0:
            flash("Must pick a release date")
            is_valid = False
        if  len(data['description']) < 3:
            flash("Description must be at least 3 characters.")
            is_valid = False
        return is_valid