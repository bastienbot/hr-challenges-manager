from pathlib import Path
from services.db import DBConnector
from services.email import EmailSender
from services.cli.input import display_and_confirm


class Template:

    def __init__(self, name, profile):
        self.name = name
        self.profile = profile
        self.rawtext = str()
        self.signature = self.load_file("signature")
        self.finaltext = self.prepare_final_text(name)
        self.db = DBConnector()

    def get_template(self):
        return self.finaltext

    def load_file(self, file):
        path = Path.cwd() / 'templates' / '{}.html'.format(file)
        return open(path).read()

    def prepare_final_text(self, name):
        self.rawtext = self.load_file(name)
        return self.replace_placeholders()

    def replace_placeholders(self):
        finaltext = self.rawtext.replace("{{firstname}}", self.profile.get("firstname"))
        finaltext = finaltext.replace("{{lastname}}", self.profile.get("lastname"))
        finaltext = finaltext.replace("{{email}}", self.profile.get("email"))
        finaltext = finaltext.replace("{{job}}", self.profile.get("job"))
        finaltext = finaltext.replace("{{signature}}", self.signature)
        return finaltext

    def send_template(self):
        user_choice = display_and_confirm(self.get_template())
        if user_choice == "Y":
            EmailSender.send(self.profile, self.get_template())
        else:
            raise Exception("Ok, email not sent. Process stopped !")

    def save_template(self):
        # self.db.save_template(self.candidate, self)
        pass
