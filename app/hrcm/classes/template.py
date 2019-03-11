from pathlib import Path
from hrcm.services.db import DBConnector
from hrcm.services.email import EmailSender
from hrcm.services.cli.input import display_and_confirm
from jinja2 import Environment, FileSystemLoader, select_autoescape, meta


class Template:

    def __init__(self, name, profile):
        self.name = name
        self.profile = profile
        self.env = Environment(
            loader=FileSystemLoader('templates/jinja'),
            autoescape=select_autoescape(['html'])
        )
        self.finaltext = self.prepare_final_text()

    def get_template(self):
        return self.finaltext

    def get_missing_variables(self):
        template_source = self.env.loader.get_source(
            self.env, '{}.html'.format(self.name))[0]
        parsed_content = self.env.parse(template_source)
        variables = meta.find_undeclared_variables(parsed_content)
        return [variable for variable in variables if variable not in self.profile]

    def prepare_final_text(self, evaluated_criterias={}):
        print(self.profile)
        print("evaluated_criterias", evaluated_criterias)
        template = self.env.get_template('{}.html'.format(self.name))
        return template.render(dict(self.profile, **evaluated_criterias))

    def send_template(self):
        EmailSender.send(self.profile, self.get_template())
