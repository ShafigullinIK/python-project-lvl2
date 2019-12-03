from gendiff.util import ADDED, CHANGED, DELETED
import json


def render_json(data):
    dict_result = prepare_dict(data)
    result = ''
    result = json.dumps(dict_result, indent=2)
    return result


def prepare_dict(data):
    return prepare_dict_rec(data, "", {
        '-': [],
        '+': [],
        '+/-': []
        }
    )


def prepare_dict_rec(data, string, d):
    for raw_key in data:
        if raw_key.find(DELETED) == 0:
            d['-'].append(string + raw_key[len(DELETED):])
        elif raw_key.find(ADDED) == 0:
            d['+'].append(string + raw_key[len(ADDED):])
        elif raw_key.find(CHANGED) == 0:
            if isinstance(data[raw_key], dict):
                d = prepare_dict_rec(
                    data[raw_key],
                    "{}{}.".format(
                        string,
                        raw_key[len(CHANGED):]
                    ),
                    d
                )
            else:
                d['+/-'].append(
                    "{}{}".format(string, raw_key[len(CHANGED):])
                )
        else:
            if isinstance(data[raw_key], dict):
                d = prepare_dict_rec(
                    data[raw_key],
                    "{}{}.".format(
                        string,
                        str(raw_key)
                    ),
                    d
                )
    return d
