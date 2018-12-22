from classes.test import TestInterface
from classes.candidate import Candidate
from services.files import FileInterface
from services.cli_options import Arguments


args = Arguments.get_arguments()
print(args)

FileInterface.create_directory("candidates")

if args["send"]:
    candidate = Candidate({
        "firstname": args["<firstname>"],
        "lastname": args["<lastname>"],
        "email": args["<email>"]
    })
    candidate.create()
    TestInterface.send_test(candidate)
