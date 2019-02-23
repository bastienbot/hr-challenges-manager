import json
from flask import request
from hrcm.classes.candidate import Candidate


class Challenges():

    def preview():
        args = request.get_json()
        job = args.get("job")
        profile = args.get("candidate")
        candidate = Candidate.load_candidate(profile.get("email"))
        candidate.job = job
        rv = candidate.preview_challenge()
        return json.dumps(rv)

    def send():
        args = request.get_json()
        job = args.get("job")
        profile = args.get("candidate")
        candidate = Candidate.load_candidate(profile.get("email"))
        candidate.job = job
        candidate.create_send_challenge()
        return json.dumps(candidate.get_profile())

    def evaluation():
        args = request.get_json()
        profile = args.get("candidate")
        candidate = Candidate.load_candidate(profile.get("email"))
        candidate.job = profile.get("job")
        evaluation = candidate.evaluate_candidate()
        return json.dumps(evaluation)
