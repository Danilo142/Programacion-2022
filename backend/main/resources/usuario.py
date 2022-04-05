from flask_restful import Resource
from flask import request

USUARIOS = {
    1 : {'firstname' : 'Joaquin', 'lastname' : 'Viñolo'},
    2 : {'firstname' : 'Martin', 'lastname' : 'Gonzales'},
    3 : {'firstname' : 'Lucas', 'lastname' : 'Ollarce'},
    4 : {'firstname' : 'Gaston', 'lastname' : 'Fenske'},
    5 : {'firstname' : 'Enzo', 'lastname' : 'Fernandez'}
}

class User(Resource):
    def get(self, id):
        if int(id) in USUARIOS:
            return USUARIOS[int(id)]
        return '', 404

    def delete(self, id):
        if int(id) in USUARIOS:
            return USUARIOS[int(id)]
        return '', 404

class Users(Resource):
    def get(self):
        return USUARIOS

    def post(self):
        user = request.get_json()
        id = int(max(USUARIOS.key())) + 1
        USUARIOS[id] = user
        return USUARIOS[id], 201