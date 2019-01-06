from .template import Template
from services.gitlab import Gitlab
from services.yaml import YamlInterface


class ChallengeInterface:

    @classmethod
    def send_challenge(cls, candidate):
        job_settings = YamlInterface.load_job_settings(candidate.job)
        if job_settings["chalenge-type"] == "default":
            return cls.__send_default_challenge(candidate, job_settings)
        elif job_settings["chalenge-type"] == "gitlab":
            return cls.__send_gitlab_challenge(candidate, job_settings)

    def __send_default_challenge(candidate, job_settings):
        template = Template(job_settings["name"], candidate=candidate)
        template.send_template()
        template.save_template()

    def __send_gitlab_challenge(candidate, job_settings):
        gitlab_api = Gitlab()
        gitlab_api.create_candidate(candidate)
        gitlab_api.fork_project_to_namespace(job_settings["id"], candidate.username)
        template = Template(job_settings["name"], candidate=candidate)
        template.send_template()
        template.save_template()
