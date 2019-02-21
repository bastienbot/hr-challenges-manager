from flask import Flask
from flask_restful import Api
from routes.index import index
from routes.candidates import Candidates
from routes.challenges import Challenges
from hrcm.errors.register import register_custom_exceptions
from jinja2 import Environment, FileSystemLoader, select_autoescape, meta


app = Flask(__name__)
api = Api(app)




def temp():
    env = Environment(
        loader=FileSystemLoader('templates/jinja'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('csm.html')
    parsed_content = env.parse(template)
    print(meta.find_undeclared_variables(parsed_content))
    return template.render({"firstname": "Bastien"})
app.add_url_rule('/temp', 'Temp', temp, methods=['GET'])




app.add_url_rule('/', 'index', index)
app.add_url_rule('/challenges/preview', 'Challenges preview', Challenges.preview, methods=['POST'])
app.add_url_rule('/challenges/send', 'Challenges send', Challenges.send, methods=['POST'])
api.add_resource(Candidates, "/candidates", "/candidates/<string:email>")

register_custom_exceptions(app)
