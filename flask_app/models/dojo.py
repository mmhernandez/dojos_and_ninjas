from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

db = "dojos_and_ninjas"

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def insert(cls, data):
        query = '''
            INSERT INTO dojos (name) 
            VALUES (%(name)s);
        '''
        connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = '''
            SELECT * 
            FROM dojos
            ORDER BY name;
        '''
        results = connectToMySQL(db).query_db(query)

        dojos = []
        for each in results:
            dojos.append(cls(each))
        
        return dojos
    
    @classmethod
    def get_one_by_id(cls, data):
        query = '''
            SELECT *
            FROM dojos
            WHERE id = %(id)s;
        '''
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = '''
            SELECT * FROM dojos D
            LEFT JOIN ninjas N ON N.dojo_id = D.id
            WHERE D.id = %(id)s
        '''
        results = connectToMySQL(db). query_db(query, data)
        dojo = cls(results[0])
        for each_row in results:
            ninja_data = {
                "id": each_row["N.id"],
                "first_name": each_row["first_name"],
                "last_name": each_row["last_name"],
                "age": each_row["age"],
                "created_at": each_row["N.created_at"],
                "updated_at": each_row["N.updated_at"]
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo
