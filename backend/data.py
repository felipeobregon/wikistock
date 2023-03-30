import json


def get_data(filename):
    with open(filename, 'r') as f:
        d = json.load(f)
        return d
