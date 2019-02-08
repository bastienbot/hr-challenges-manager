from flask import Flask
from flask_restful import Api
from routes.candidates import Candidates
from hrcm.errors.register import register_custom_exceptions


app = Flask(__name__)
api = Api(app)

api.add_resource(Candidates, "/candidates", "/candidates/<string:email>")
@app.route("/")
def hello():
    return "Zog zog"

register_custom_exceptions(app)
