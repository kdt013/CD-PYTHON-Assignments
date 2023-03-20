query = "INSERT INTO friends {first_name, last_name, email) VALUES ( %(first_name)s, %(last_name)s, %(email)s );"

data = {
    "first_name": "Kavita",
    "last_name": "Thomas",
    "email": "kthomas@codingdojo.com"
}