from services.gitlab import Gitlab
from services.yaml import load_tt_informations


class TestInterface:

    def send_test(candidate):
        gitlab_api = Gitlab()
        gitlab_api.create_candidate(candidate)
        tt_informations = load_tt_informations()
        project_id = tt_informations[candidate.job]["id"]
        gitlab_api.fork_project_to_namespace(project_id, candidate.username)
