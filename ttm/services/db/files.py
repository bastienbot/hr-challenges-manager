import os
import json
import shutil
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
        DBFiles.create_directory("candidates/{}".format(candidate.email))
        DBFiles.create_file_with_content(
            path="candidates/{}/profile.json".format(candidate.email),
            content="{}".format(json.dumps(candidate.get_profile()))
        )
        return candidate

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