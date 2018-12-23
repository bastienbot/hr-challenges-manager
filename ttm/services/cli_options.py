"""Technical test Manager

Usage:
  ttm send <firstname> <lastname> <email> <job>
  ttm show <email>
  ttm remove <email>

Options:
  -h --help     Show this screen.
  --version     Show version.
"""
from docopt import docopt


class Arguments:

    def get_arguments():
        return docopt(__doc__, version='Technical test Manager 0.1a')
