"""HR challenge Manager

Usage:
  hrcm send <firstname> <lastname> <email> <job>
  hrcm candidates
  hrcm show <email>
  hrcm delete <email>

Options:
  -h --help     Show this screen.
  --version     Show version.
"""
from docopt import docopt


class Arguments:

    def get_arguments():
        return docopt(__doc__, version='HR challenge Manager 0.1a')
