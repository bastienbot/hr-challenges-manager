import os
import json
from datetime import datetime
from services.db import DBConnector
from services.files import FileInterface
from helpers import normalize_dict, format_username


class Candidate:

    """
    @desc We prepare all the instance parameters along side the db instance

    @params informations: a lsit of cli parameters
    @returns
    """
    def __init__(self, informations):
        normalize_dict(informations, {"archived": False})
        self.firstname = informations["firstname"]
        self.lastname = informations["lastname"]
        self.email = informations["email"]
        self.job = informations["job"]
        self.phone = str()
        self.username = format_username(informations["firstname"], informations["lastname"])
        self.messages = list()
        self.archived = informations["archived"]
        self.db = DBConnector()

    def get_messages(self):
        self.messages = self.db.get_messages(self)
        return self

    def create(self):
        self.db.create_candidate(self)
        print("User created successfuly")
        return self

    def delete(self):
        self.db.delete_candidate(self)
        print("User deleted successfuly")
        return self

    def archive(self):
        self.archived = True
        self.db.save_profile(self)
        print("Candidate archived")
        return self

    def get_profile(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "job": self.job,
            "phone": self.phone,
            "username": self.username,
            "archived": self.archived
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
            The archive option tells if the method returns the (non-)archived candidates

    @params: archive: bool
    @returns [instance of Candidate]
    """
    @classmethod
    def load_candidates(cls, archive=False):
        db = DBConnector()
        emails = db.get_candidates_emails()
        candidates = [cls(db.get_profile_by_email(email)) for email in emails]
        return [candidate.get_messages() for candidate in candidates if candidate.archived == archive]
