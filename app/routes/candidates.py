from flask import request
from flask_restful import Resource
from hrcm.classes.candidate import Candidate
from hrcm.errors.resource_not_found import ResourceNotFound


class Candidates(Resource):

    def get(self, email):
        print(email)
        candidate = Candidate.load_candidate(email)
        try:
            return candidate.get_profile()
        except:
            raise ResourceNotFound("This candidate does not exist.")

    def post(self):
        args = request.get_json()
        candidate = Candidate(args)
        candidate.save()
        return candidate.get_profile()

    def put(self):
        return "put endpoint"

    def delete(self):
        return "delete endpoint"
