import os
import json
from datetime import datetime
from .challenge import Challenge
from services.db import DBConnector
from helpers import format_username


class Candidate:

    """
    @desc We prepare all the instance parameters along side the db instance

    @params informations: a list of cli parameters
    @returns
    """
    def __init__(self, informations):
        self.id = informations.get("_id")
        self.firstname = informations.get("firstname")
        self.lastname = informations.get("lastname")
        self.email = informations.get("email")
        self.job = informations.get("job")
        self.phone = informations.get("phone", str())
        self.username = format_username(
            informations.get("firstname"),
            informations.get("lastname")
        )
        self.messages = informations.get("messages", list())
        self.archived = informations.get("archived", False)
        self.challenge = None
        self.db = DBConnector()

    def get_messages(self):
        self.messages = self.db.get_messages(self)
        return self

    """
    @desc This methods create a new candidate and adds its id to self when
            the DB requires an id

    @params self: instance of Candidate
    @returns instance of Candidate
    """
    def save(self):
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

    def create_send_challenge(self):
        self.challenge = Challenge()
        self.challenge.send_challenge(self)
        self.messages = self.challenge.get_sent_messages()

    def get_profile(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "job": self.job,
            "phone": self.phone,
            "messages": self.messages,
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
        return [cls(candidate) for candidate in db.get_profiles(archived=False)]
