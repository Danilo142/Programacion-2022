from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import CalificacionModel


class Qualification(Resource):
   def get(self, id):
        qualification = db.session.query(CalificacionModel).get_or_404(id)
        return qualification.to_json()

   def delete(self, id):
        qualification = db.session.query(CalificacionModel).get_or_404(id)
        db.session.delete(qualification)
        db.session.commit()
        return '', 204


class Califications(Resource):
    def get(self):
        qualifications = db.session.query(CalificacionModel).all()
        return jsonify([qualification.to_json_short() for qualification in qualifications])


    def post(self):
         qualification = CalificacionModel.from_json(request.get_json())
         db.session.add(qualification)
         db.session.commit()
         return qualification.to_json(), 201
