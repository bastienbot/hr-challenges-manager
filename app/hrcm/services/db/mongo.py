import json
import datetime
from time import time
from .base import DBBase
from pymongo import MongoClient


class DBMongo(DBBase):

    """
    @desc Operations to be done as we create the instance, in this case we create a candidate folder
    """
    def __init__(self):
        self.client = MongoClient('mongodb://root:example@mongo:27017/')
        self.db = self.client.hrcm
        self.candidates_col = self.db.candidates

    """
    @desc Create new candidate. We need to stringify the inserted_id in order to be able
            to serialize it as json.
            As of now we wamt to be able to duplicate a candidate as people might want to
            apply for several jobs.

    @params candidate: instance of Candidate
    @returns instance of Candidate
    """
    def create_candidate(self, candidate):
        doc = self.candidates_col.insert_one(candidate.get_profile(show_id=False))
        candidate._id = str(doc.inserted_id)
        return candidate

    def delete_candidate(self, candidate):
        query = {"_id": candidate._id} if candidate._id is not None else {"email": candidate.email}
        self.candidates_col.delete_one(query)

    """
    @desc We need to remove the id key from the candidate instance as mongo would otherwise
            try to save it

    @params candidate: instance of Candidate
    @returns None
    """
    def update_candidate(self, candidate):
        filter_param = {"_id": candidate._id}
        profile = candidate.get_profile(show_id=False)
        query = {"$set": profile}
        self.candidates_col.update_one(filter_param, query)

    """
    @desc Saves the sent email

    @params candidate: instance of Candidate
    @params template: instance of Template
    @returns
    """
    def save_template(self, candidate, template):
        pass

    def get_profile_by_email(self, email):
        profile = self.candidates_col.find_one({"email": email})
        return profile

    def get_profiles(self, archived):
        profiles = self.candidates_col.find()
        return profiles
