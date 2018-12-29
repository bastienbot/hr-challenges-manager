import settings
from classes.template import Template
from classes.test import TestInterface
from classes.candidate import Candidate
from services.gitlab import Gitlab
from services.cli_options import Arguments


args = Arguments.get_arguments()

if args["send"]:
    candidate = Candidate({
        "firstname": args["<firstname>"],
        "lastname": args["<lastname>"],
        "email": args["<email>"],
        "job": args["<job>"]
    })
    candidate.create()
    TestInterface.send_test(candidate)
    template = Template(name="new_test", candidate=candidate)
    template.send_template()
    template.save_template()
    print("All done !")
elif args["show"]:
    try:
        candidate = Candidate.load_candidate(args["<email>"])
        print(candidate.get_profile())
    except Exception as e:
        print(e)
elif args["delete"]:
    try:
        candidate = Candidate.load_candidate(args["<email>"])
        candidate.delete()
    except Exception as e:
        print(e)
