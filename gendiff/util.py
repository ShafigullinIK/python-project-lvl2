import os.path
import json
import yaml


DELETED = ' deleted '
ADDED = '  added  '
CHANGED = ' changed '
DEVIDER = "~|~"


def normalize_path(path_to_file):
    return os.path.abspath(path_to_file)


def load_from_file(path_to_file):
    file_type = path_to_file.split('.')[-1]
    if(file_type == 'json'):
        return load_from_json_file(path_to_file)
    if(file_type == 'yml'):
        return load_from_yaml_file(path_to_file)


def load_from_json_file(path_to_file):
    return json.load(open(normalize_path(path_to_file)))


def load_from_yaml_file(path_to_file):
    return yaml.load(open(normalize_path(path_to_file)))
