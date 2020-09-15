import yaml
from os import path


BASE_DIR = path.dirname(path.abspath(__file__))

def read_config(BASE_DIR: str) -> dict:
    with open(path.join(BASE_DIR, 'config.yaml')) as myyaml:
        ENVIRONMENT = yaml.safe_load(myyaml)
    return ENVIRONMENT

ENVIRONMENT = read_config(BASE_DIR)