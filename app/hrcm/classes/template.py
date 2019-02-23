from pathlib import Path
from hrcm.services.db import DBConnector
from hrcm.services.email import EmailSender
from hrcm.services.cli.input import display_and_confirm
from jinja2 import Environment, FileSystemLoader, select_autoescape, meta


class Template:

    def __init__(self, name, profile):
        self.name = name
        self.profile = profile
        self.finaltext = self.prepare_final_text(name)
        self.env = Environment(
            loader=FileSystemLoader('templates/jinja'),
            autoescape=select_autoescape(['html'])
        )

    def get_template(self):
        return self.finaltext

    def load_file(self, file):
        path = Path.cwd() / 'templates' / '{}.html'.format(file)
        return open(path).read()

    def get_missing_variables(self):
        template_source = self.env.loader.get_source(self.env, '{}.html'.format(self.name))[0]
        parsed_content = self.env.parse(template_source)
        variables = meta.find_undeclared_variables(parsed_content)
        return [variable for variable in variables if variable not in self.profile]

    def prepare_final_text(self, name):
        template = self.env.get_template('{}.html'.format(self.name))
        return template.render({"firstname": "Bastien"})

    def send_template(self):
        EmailSender.send(self.profile, self.get_template())
