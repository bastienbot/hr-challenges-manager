import json
from services.files import FileInterface


class Candidate:

    def __init__(self, informations):
        self.firstname = informations["firstname"]
        self.lastname = informations["lastname"]
        self.email = informations["email"]
        self.phone = ""

    def create(self):
        FileInterface.create_directory("candidates/{}".format(self.email))
        FileInterface.create_file_with_content(
            path="candidates/{}/profile.json".format(self.email),
            content="{}".format(json.dumps(self.__dict__))
        )
        print("User created successfuly")

    def remove(self):
        print("User not yet removed")
