from routes.candidates import Candidates
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(Candidates, "/candidates")


@app.route("/")
def hello():
    return "Zog zog"
