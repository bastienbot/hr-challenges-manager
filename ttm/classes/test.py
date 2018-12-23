import json
from services.gitlab import Gitlab


class TestInterface:

    def send_test(candidate):
        gitlab_api = Gitlab()
        gitlab_api.create_candidate(candidate)
