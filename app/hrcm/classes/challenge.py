from time import time
from .template import Template
from hrcm.services.gitlab import Gitlab
from hrcm.services.yaml import YamlInterface
from hrcm.helpers import variable_to_question


class Challenge:

    def __init__(self):
        self.processed = False
        self.sent_messages = list()

    def preview_challenge(self, candidate):
        job_settings = YamlInterface.load_job_settings(candidate.job)
        if job_settings["chalenge-type"] == "default":
            return self.__preview_default_challenge(candidate, job_settings)
        elif job_settings["chalenge-type"] == "gitlab":
            return self.__preview_gitlab_challenge(candidate, job_settings)

    def send_challenge(self, candidate):
        job_settings = YamlInterface.load_job_settings(candidate.job)
        if job_settings["chalenge-type"] == "default":
            self.__send_default_challenge(candidate, job_settings)
        elif job_settings["chalenge-type"] == "gitlab":
            self.__send_gitlab_challenge(candidate, job_settings)
        self.processed = True

    def get_sent_messages(self):
        return self.sent_messages

    def get_evalution_criterias(self, candidate):
        job_settings = YamlInterface.load_job_settings(candidate.job)
        template = Template(job_settings["name"], candidate.get_profile())
        return [{
            "variable": variable,
            "question": variable_to_question(variable)}
            for variable in template.get_missing_variables()]

    def __send_default_challenge(self, candidate, job_settings):
        self.__send_save_template(candidate, job_settings["name"])

    def __send_gitlab_challenge(self, candidate, job_settings):
        gitlab_api = Gitlab()
        gitlab_api.create_candidate(candidate)
        gitlab_api.fork_project_to_namespace(
            job_settings["id"],
            candidate.username)
        self.__send_save_template(candidate, job_settings["name"])

    def __send_save_template(self, candidate, name):
        template = Template(name, candidate.get_profile())
        template.send_template()
        self.sent_messages.append({
            "text": template.get_template(),
            "created_at": time(),
            "name": name})

    def __preview_default_challenge(self, candidate, job_settings):
        template = Template(job_settings["name"], candidate.get_profile())
        return {"template": template.get_template()}

    def __preview_gitlab_challenge(self, candidate, job_settings):
        template = Template(job_settings["name"], candidate.get_profile())
        gitlab_api = Gitlab()
        project = gitlab_api.get_project_info(job_settings["id"])
        return {"project": project, "template": template.get_template()}

    def _evalate_challenge(self):
        pass
