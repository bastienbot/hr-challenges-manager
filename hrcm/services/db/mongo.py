import json
import datetime
from time import time
from .base import DBBase
from pymongo import MongoClient


class DBMongo(DBBase):

    """
    @desc Operations to be done as we create the instance, in this case we create a candidate folder

    @params
    @returns
    """
    def __init__(self):
        self.client = MongoClient('mongodb://root:example@mongo:27017/')
        self.db = self.client.hrcm
        self.candidates_col = self.db.candidates

    """
    @desc Create new candidate

    @params instance of Candidate
    @returns instance of Candidate
    """
    def create_candidate(self, candidate):
        doc = self.candidates_col.insert_one(candidate.get_profile())
        candidate.id = doc.inserted_id
        return candidate

    def delete_candidate(self, candidate):
        query = {"_id": candidate.id} if candidate.id is not None else {"email": candidate.email}
        self.candidates_col.delete_one(query)

    # """
    # @desc Saves the sent email

    # @params candidate: instance of Candidate
    # @params template: instance of Template
    # @returns
    # """
    def save_template(self, candidate, template):
        pass

    def get_profile_by_email(self, email):
        profile = self.candidates_col.find_one({"email": email})
        return profile

    def get_profiles(self):
        profiles = self.candidates_col.find()
        return profiles

    def save_profile(self, candidate):
        pass
