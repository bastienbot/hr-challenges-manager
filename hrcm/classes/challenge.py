from time import time
from .template import Template
from services.gitlab import Gitlab
from services.yaml import YamlInterface


class Challenge:

    def __init__(self):
        self.processed = False
        self.sent_messages = list()

    def send_challenge(self, candidate):
        job_settings = YamlInterface.load_job_settings(candidate.job)
        if job_settings["chalenge-type"] == "default":
            self.__send_default_challenge(candidate, job_settings)
        elif job_settings["chalenge-type"] == "gitlab":
            self.__send_gitlab_challenge(candidate, job_settings)
        self.processed = True

    def get_sent_messages(self):
        return self.sent_messages

    def __send_default_challenge(self, candidate, job_settings):
        self.__send_save_template(candidate, job_settings["name"])

    def __send_gitlab_challenge(self, candidate, job_settings):
        gitlab_api = Gitlab()
        gitlab_api.create_candidate(candidate)
        gitlab_api.fork_project_to_namespace(job_settings["id"], candidate.username)
        self.__send_save_template(candidate, job_settings["name"])

    def __send_save_template(self, candidate, name):
        template = Template(name, candidate.get_profile())
        template.send_template()
        self.sent_messages.append({"message": template.get_template(), "created_at": time()})
