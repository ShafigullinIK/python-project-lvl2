import os.path
import json
import yaml


def normalize_path(path_to_file):
    return os.path.abspath(path_to_file)


def load_from_file(path_to_file):
    file_type = path_to_file.split('.')[-1]
    load = load_from_json_file  # noqa Вариант по умолчанию, чтобы не падать из-за пустой функции
    if file_type == 'json':
        load = load_from_json_file
    if file_type == 'yml':
        load = load_from_yaml_file
    return load(path_to_file)


def load_from_json_file(path_to_file):
    return json.load(open(os.path.abspath(path_to_file)))


def load_from_yaml_file(path_to_file):
    return yaml.load(open(os.path.abspath(path_to_file)))
