import yaml
from pathlib import Path


class YamlInterface:

    @classmethod
    def load_job_settings(cls, job):
        jobs_settings = cls.__load_tc_informations()
        try:
            return jobs_settings[job]
        except:
            raise Exception("This job does not exist: {}".format(job))

    def __load_tc_informations():
        path = Path.cwd() / 'tc_informations.yaml'
        try:
            f = open(path, "r")
            return yaml.load(f)
        except:
            raise Exception("Yaml jobs setting file does not exist: {}".format(path))
