import settings
from services.cli_options import Arguments
from classes.candidate import Candidate
from classes.challenge import ChallengeInterface
from services.output import show_candidate_informations


args = Arguments.get_arguments()

if args["send"]:
    candidate = Candidate({
        "firstname": args["<firstname>"],
        "lastname": args["<lastname>"],
        "email": args["<email>"],
        "job": args["<job>"]
    })
    candidate.create()
    ChallengeInterface.send_challenge(candidate)
    print("All done !")
elif args["show"]:
    try:
        candidate = Candidate.load_candidate(args["<email>"])
        candidate.get_messages()
        show_candidate_informations(candidate)
    except Exception as e:
        print(e)
elif args["delete"]:
    try:
        candidate = Candidate.load_candidate(args["<email>"])
        candidate.delete()
    except Exception as e:
        print(e)
