from pathlib import Path


class Template:

    def __init__(self, name, candidate):
        self.name = name
        self.candidate = candidate
        self.rawtext = str
        self.signature = self.load_file("signature")
        self.finaltext = self.prepare_final_text(name)

    def get_template(self):
        return self.finaltext

    def load_file(self, file):
        path = Path.cwd() / 'templates' / '{}.html'.format(file)
        return open(path).read()

    def prepare_final_text(self, name):
        self.rawtext = self.load_file(name)
        return self.replace_placeholders()

    def replace_placeholders(self):
        finaltext = self.rawtext.replace("{{firstname}}", self.candidate.firstname)
        finaltext = finaltext.replace("{{lastname}}", self.candidate.lastname)
        finaltext = finaltext.replace("{{email}}", self.candidate.email)
        finaltext = finaltext.replace("{{job}}", self.candidate.job)
        finaltext = finaltext.replace("{{signature}}", self.signature)
        return finaltext
