from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Travel_Plans:
    def __init__( self , data ):
        self.id = data['id']
        self.destination = data['destination']
        self.arrival_date = data['arrival_date']
        self.departure_date = data['departure_date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']


    @classmethod
    def get_all_travel_plans(cls):
        query= "SELECT * FROM travel_plans JOIN users on travel_plans.users_id = users.id;"
        results = connectToMySQL("travels").query_db(query)

        travel_plans = []

        for row_from_db in results:
            one_plan = cls(row_from_db)
            data = {
                "id": row_from_db["users.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "email": row_from_db["email"],
                "password": row_from_db["password"],
                "created_at": row_from_db["users.created_at"],
                "updated_at": row_from_db["users.updated_at"]
                }
            one_plan.id_of_plan = User(data)

            travel_plans.append(one_plan)
        return travel_plans

    @classmethod
    def save(cls,data):
        query = "INSERT INTO travel_plans (destination, arrival_date, departure_date, created_at, updated_at, users_id) VALUES (%(destination)s, %(arrival_date)s, %(departure_date)s, NOW(), NOW(), %(users_id)s);"

        travel_plan_id = connectToMySQL("travels").query_db(query,data)
        return travel_plan_id