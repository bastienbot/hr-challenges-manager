import os
import json
import requests
from time import sleep


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
                "username": user.username,
                "name": user.username,
                "can_create_group": False,
                "external": True
            })
        print(r.content)

    def create_candidate(self, candidate):
        self.create_user(candidate, external=True)

    def fork_project_to_namespace(self, project_id, namespace):
        r = requests.post(
            url="{}/projects/{}/fork".format(self.url, project_id),
            headers=self.headers,
            json={
                "namespace": namespace
            })
        print(r.content)

    def get_project_info(self, project_id):
        r = requests.get(
            url="{}/projects/{}".format(self.url, project_id),
            headers=self.headers)
        res = json.loads(r.content)
        return {"name": res.get("name_with_namespace"), "url": res.get("web_url")}
