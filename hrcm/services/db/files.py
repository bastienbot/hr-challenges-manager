import os
import json
import shutil
import datetime
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
        DBFiles.save_profile(candidate)
        return candidate

    def delete_candidate(self, candidate):
        path = "candidates/{}".format(candidate.email)
        DBFiles.delete_directory(path)

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
        try:
            raw_profile = open(path).read()
        except:
            raise Exception("This candidate does not exist")
        return json.loads(raw_profile)

    def get_candidates_emails(self):
        return DBFiles.list_files(path='candidates')

    def save_profile(self, candidate):
        DBFiles.create_file_with_content(
            path="candidates/{}/profile.json".format(candidate.email),
            content="{}".format(json.dumps(candidate.get_profile()))
        )

    """
    @desc We fetch the files list from the candidate folder,
            and we format the files to get the timestamps and messages names
    @returns [ { name: str, timestamp: str } ]
    """
    def get_messages(self, candidate):
        files = DBFiles.list_files(path='candidates/{}'.format(candidate.email))
        messages = []
        for f in files:
            if f != "profile.json":
                f = f.split("-", 1)
                messages.append({
                    "timestamp": f[0],
                    "ts_str": datetime.datetime.utcfromtimestamp(int(float(f[0]))).strftime('%d-%m-%Y %H:%M:%S'),
                    "diff_to_today": int(int(time() - int(float(f[0]))) / 60 / 60 / 24),
                    "name": f[1]
                })
        return messages

    """
    @desc Creates a candidate directory if it does not exist already

    @params candidate: instance of candidate
    """
    @staticmethod
    def create_candidate_folder_if_not_exists(candidate):
        DBFiles.create_directory("candidates/{}".format(candidate.email))

    @staticmethod
    def create_directory(path):
        if not os.path.isdir("./{}".format(path)):
            os.makedirs("./{}".format(path))

    @staticmethod
    def list_files(path):
        return os.listdir(path=path)

    @staticmethod
    def delete_directory(path):
        try:
            shutil.rmtree("./{}".format(path))
        except Exception as e:
            raise e

    @staticmethod
    def create_file_with_content(path, content):
        f = open(path, "w+")
        f.write(content)
        f.close()

    @staticmethod
    def copy_file(source, dest):
        shutil.copyfile(source, dest)