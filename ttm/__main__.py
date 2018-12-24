import settings
from classes.template import Template
from classes.test import TestInterface
from classes.candidate import Candidate
from services.gitlab import Gitlab
from services.files import FileInterface
from services.cli_options import Arguments
from services.email import EmailSender


args = Arguments.get_arguments()

FileInterface.create_directory("candidates")

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
    EmailSender.send(candidate, template)
    print("All done !")
