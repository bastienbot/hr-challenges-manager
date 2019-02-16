from flask import request


class Challenges():

    def preview():
        args = request.get_json()
        job = args.get("job")
        candidate = args.get("candidate")
        return str(args)

    def send():
        pass
