from flask import request
from flask_restful import Resource
from hrcm.classes.candidate import Candidate
from hrcm.errors.resource_not_found import ResourceNotFound


class Candidates(Resource):

    def get(self, email):
        candidate = Candidate.load_candidate(email)
        if candidate is not None:
            return candidate.get_profile()
        else:
            raise ResourceNotFound("This candidate does not exist.")

    def post(self):
        args = request.get_json()
        candidate = Candidate(args)
        candidate.create()
        return candidate.get_profile()

    def put(self):
        args = request.get_json()
        candidate = Candidate.load_candidate(args["email"])
        if candidate is not None:
            [setattr(candidate, key, args.get(key)) for key in args.keys()]
            candidate.update()
            return candidate.get_profile()
        else:
            raise ResourceNotFound("This candidate does not exist.")

    def delete(self):
        return "delete endpoint"
