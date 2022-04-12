from flask_restful import Resource
from flask import request

#Prueba 
POEMS = {
    1 : {'Titulo' : 'La cancion del pirata' ,'Autor' : 'Jose de Espronceda'},
    2 : {'Titulo' : 'A una rosa' ,'Autor' : 'Gongora'},
    3 : {'Titulo' : 'Ir y quedarse' ,'Autor' : 'Lope de Vega'},
    4 : {'Titulo' : 'Hija del viento' ,'Autor' : 'Alejandra Pizarnik'},
    5 : {'Titulo' : 'El remordimiento' ,'Autor' : 'Jorge Luis Borges'}
}

class Poem(Resource):
    def get(self, id):
        if int(id) in POEMS:
            return POEMS[int(id)]
        return '', 404

    def delete(self, id):
        if int(id) in POEMS:
            return POEMS[int(id)]
        return '', 404

class Poems(Resource):
    def get(self):
        return POEMS

    def post(self):
        poem = request.get_json()
        id = int(max(POEMS.key())) + 1
        POEMS[id] = poem
        return POEMS[id], 201