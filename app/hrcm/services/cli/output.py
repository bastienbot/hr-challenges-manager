"""
@desc Prints informations about the candidate : his/her profile and messages sent

@params candidate: instance of Candidate
"""


def show_candidate_informations(candidate):
    print("## CANDIDATE PROFILE ##", end="\n\n")
    print("Firstname: {}".format(candidate.firstname))
    print("Lastname: {}".format(candidate.lastname))
    print("Email address: {}".format(candidate.email))
    print("Job: {}".format(candidate.job), end="\n\n")
    print("## MESSAGE SENT ##", end="\n\n")
    for message in candidate.messages:
        print("{0} sent : {1}, {2} days ago".format(
            message["name"],
            message["ts_str"],
            message["diff_to_today"])
        )


def show_candidates(candidates):
    for candidate in candidates:
        print("\nFirstname: {0}, Lastname: {1}, Email address: {2}, Job: {3}".format(candidate.firstname, candidate.lastname, candidate.email, candidate.job))
        for message in candidate.messages:
            print("\t{0} sent : {1}, {2} days ago".format(
                message["name"],
                message["ts_str"],
                message["diff_to_today"])
            )
