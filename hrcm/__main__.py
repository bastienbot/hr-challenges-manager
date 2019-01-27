import settings
from services.cli.options import Arguments
from classes.candidate import Candidate
from classes.challenge import ChallengeInterface
from services.cli.output import show_candidate_informations, show_candidates


args = Arguments.get_arguments()

if args["send"]:
    candidate = Candidate({
        "firstname": args["<firstname>"],
        "lastname": args["<lastname>"],
        "email": args["<email>"],
        "job": args["<job>"]
    })
    ChallengeInterface.send_challenge(candidate)
    candidate.create()
    print("All done !")
elif args["archive"]:
    try:
        candidate = Candidate.load_candidate(args["<email>"])
        candidate.archive()
    except Exception as e:
        print(e)
elif args["candidates"]:
    try:
        candidates = Candidate.load_candidates(archive=False)
        show_candidates(candidates)
    except Exception as e:
        print(e)
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
