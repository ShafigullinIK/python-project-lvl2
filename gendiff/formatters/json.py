from gendiff.parsers import ADDED, CHANGED, DELETED, NORMAL
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
        (pref, key) = raw_key
        if pref == DELETED:
            d['-'].append(string + key)
        elif pref == ADDED:
            d['+'].append(string + key)
        elif pref == CHANGED:
            if isinstance(data[raw_key], dict):
                d = prepare_dict_rec(
                    data[raw_key],
                    "{}{}.".format(
                        string,
                        key
                    ),
                    d
                )
            else:
                d['+/-'].append(
                    "{}{}".format(string, key)
                )
        elif pref == NORMAL:
            if isinstance(data[raw_key], dict):
                d = prepare_dict_rec(
                    data[raw_key],
                    "{}{}.".format(
                        string,
                        key
                    ),
                    d
                )
    return d
