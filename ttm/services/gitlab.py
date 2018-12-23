import os
import requests


class Gitlab:

    def __init__(self):
        self.GITLAB_TOKEN = os.getenv("GITLAB_TOKEN")
        self.GITLAB_URL = os.getenv("GITLAB_URL")
        self.GITLAB_URI = "/api/v4"
        self.url = "{}{}".format(self.GITLAB_URL, self.GITLAB_URI)
        self.headers = {'Private-Token': self.GITLAB_TOKEN}

    def create_user(self, user, external=False):
        r = requests.get("{}/projects".format(self.url), headers=self.headers)
        print(r.content)
        # r = requests.post(
        #     "{}/detect_vary_templates".format(self.host),
        #     json={"text": "Qui est le boss",
        #           "templates": datas.templates})
        # self.assertEqual(r.status_code, 200)
        # res = json.loads(r.content)

    def create_candidate(self, candidate):
        self.create_user(candidate, external=True)
