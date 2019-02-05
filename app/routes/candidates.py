from flask import request
from flask_restful import Resource
from hrcm.classes.candidate import Candidate


class Candidates(Resource):
    def get(self):
        return "get endpoint"

    def post(self):
        args = request.get_json()
        candidate = Candidate(args)
        candidate.save()
        return candidate.get_profile()

    def put(self):
        return "put endpoint"

    def delete(self):
        return "delete endpoint"
