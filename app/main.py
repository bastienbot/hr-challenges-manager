from flask import Flask
from flask_restful import Api
from routes.index import index
from routes.candidates import Candidates
from routes.challenges import Challenges
from hrcm.errors.register import register_custom_exceptions


app = Flask(__name__)
api = Api(app)

app.add_url_rule('/', 'index', index)
app.add_url_rule('/challenges/preview', 'Challenges preview', Challenges.preview, methods=['POST'])
api.add_resource(Candidates, "/candidates", "/candidates/<string:email>")

register_custom_exceptions(app)
