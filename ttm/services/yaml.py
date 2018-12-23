import os
import yaml
from pathlib import Path


def load_tt_informations():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = Path(dir_path).parent.parent / 'tt_informations.yaml'
    f = open(path, "r")
    return yaml.load(f)
