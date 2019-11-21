import os.path
import json


def normalize_path(path_to_file):
    return os.path.abspath(path_to_file)


def load_from_json_file(path_to_file):
    return json.load(open(normalize_path(path_to_file)))
