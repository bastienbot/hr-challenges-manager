import os
import json
import shutil
from time import time
from .base import DBBase


class DBFiles(DBBase):

    """
    @desc Operations to be done as we create the instance, in this case we create a candidate folder

    @params
    @returns
    """
    def __init__(self):
        self.create_directory("candidates")

    """
    @desc Create new candidate

    @params instance of Candidate
    @returns instance of Candidate
    """
    def create_candidate(self, candidate):
        DBFiles.create_candidate_folder_if_not_exists(candidate)
        DBFiles.create_file_with_content(
            path="candidates/{}/profile.json".format(candidate.email),
            content="{}".format(json.dumps(candidate.get_profile()))
        )
        return candidate

    """
    @desc Saves the sent email

    @params candidate: instance of Candidate
    @params template: instance of Template
    @returns
    """
    def save_template(self, candidate, template):
        DBFiles.create_candidate_folder_if_not_exists(candidate)
        DBFiles.create_file_with_content(
            path="candidates/{}/{}-{}.html".format(
                candidate.email,
                time(),
                template.name
            ),
            content=template.get_template()
        )
        return candidate

    def get_profile_by_email(self, email):
        path = "candidates/{}/profile.json".format(email)
        raw_profile = open(path).read()
        return json.loads(raw_profile)

    """
    @desc Creates a candidate directory if it does not exist already

    @params candidate: instance of candidate
    """
    @staticmethod
    def create_candidate_folder_if_not_exists(candidate):
        DBFiles.create_directory("candidates/{}".format(candidate.email))

    @staticmethod
    def create_directory(name):
        if not os.path.isdir("./{}".format(name)):
            os.makedirs("./{}".format(name))

    @staticmethod
    def create_file_with_content(path, content):
        f = open(path, "w+")
        f.write(content)
        f.close()

    @staticmethod
    def copy_file(source, dest):
        shutil.copyfile(source, dest)