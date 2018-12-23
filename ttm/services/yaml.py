import yaml
from pathlib import Path


def load_tt_informations():
    path = Path.cwd() / 'tt_informations.yaml'
    f = open(path, "r")
    return yaml.load(f)
