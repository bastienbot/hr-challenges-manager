import json
from services.db import DBConnector


class Candidate:

    """
    @desc We prepare all the instance parameters along side the db instance

    @params informations: a lsit of cli parameters
    @returns
    """
    def __init__(self, informations):
        self.firstname = informations["firstname"]
        self.lastname = informations["lastname"]
        self.email = informations["email"]
        self.job = informations["job"]
        self.phone = ""
        self.username = "{}.{}.external".format(self.firstname, self.lastname).lower()
        self.db = DBConnector()

    def get_profile(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "job": self.job,
            "phone": self.phone,
            "username": self.username
        }

    def create(self):
        self.db.create_candidate(self)
        print("User created successfuly")

    def delete(self):
        self.db.delete_candidate(self)
        print("User deleted successfuly")

    """
    @desc Get the candidate profile and returns an instance of Candidate

    @params email: str
    @returns instance of Candidate
    """
    @staticmethod
    def load_candidate(email):
        db = DBConnector()
        profile = db.get_profile_by_email(email)
        return Candidate(profile)
