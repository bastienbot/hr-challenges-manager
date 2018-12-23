import os
import requests


class Gitlab:

    GITLAB_TOKEN = os.getenv("GITLAB_TOKEN")
    GITLAB_URL = os.getenv("GITLAB_URL")
    GITLAB_URI = "/api/v4"

    def __init__(self):
        self.url = "{}{}".format(self.GITLAB_URL, self.GITLAB_URI)
        self.headers = {'Private-Token': self.GITLAB_TOKEN}

    def create_user(self, user, external=False):
        # TODO: We should check if the username is free before sending
        r = requests.post(
            url="{}/users".format(self.url),
            headers=self.headers,
            json={
                "email": user.email,
                "reset_password": True,
                "username": "{}.{}.external".format(user.firstname, user.lastname),
                "name": "{}.{}.external".format(user.firstname, user.lastname),
                "can_create_group": False,
                "external": True
            })
        print(r.content)
        # res = json.loads(r.content)

    def create_candidate(self, candidate):
        self.create_user(candidate, external=True)

    def fork_project(self, project_id):
        r = requests.post(
            url="{}/projects/{}/fork".format(self.url, project_id),
            headers=self.headers)
        print(r.content)
