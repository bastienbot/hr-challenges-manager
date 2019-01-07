import os
import json
from datetime import datetime
from services.db import DBConnector
from services.files import FileInterface


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
        self.phone = str()
        self.username = "{}.{}.external".format(self.firstname, self.lastname).lower()
        self.messages = list()
        self.db = DBConnector()

    def get_messages(self):
        self.messages = self.db.get_messages(self)

    def create(self):
        self.db.create_candidate(self)
        print("User created successfuly")

    def delete(self):
        self.db.delete_candidate(self)
        print("User deleted successfuly")

    def get_profile(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "job": self.job,
            "phone": self.phone,
            "username": self.username
        }

    """
    @desc Get the candidate profile and returns an instance of Candidate

    @params email: str
    @returns instance of Candidate
    """
    @classmethod
    def load_candidate(cls, email):
        db = DBConnector()
        profile = db.get_profile_by_email(email)
        return cls(profile)

    """
    @desc Get all the candidates and return an list of Candidate instances

    @returns [instance of Candidate]
    """
    @classmethod
    def load_candidates(cls):
        db = DBConnector()
        emails = db.get_candidates_emails()
        return [cls(db.get_profile_by_email(email)) for email in emails]
