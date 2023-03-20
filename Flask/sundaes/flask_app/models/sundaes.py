from flask_app.config.mysqlconnection import connectToMySQL

class Sundae:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.flavor = data["flavor"]
        self.num_scoops = data["num_scoops"]
        self.topping = data["topping"]
        self.sauce = data["sauce"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        @classmethod
        def get_all(cls):
            query = "SELECT * FROM sundaes;"
            results = connectToMySQL("sundaes_demo_september2022").query_db(query)

            sundaes = []
            for result in results:
                one_instance = cls(result)
                sundaes.append(one_instance)
            return sundaes