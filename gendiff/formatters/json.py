from gendiff.util import ADDED, CHANGED, DELETED
import json


dict_result = {
    '-': [],
    '+': [],
    '+/-': []
    }


def render_json(data):
    render_plain(data)
    result = ''
    result = json.dumps(dict_result, indent=2)
    return result


def render_plain(data):
    render_plain_rec(data, "")
    return dict_result


def render_plain_rec(data, string):
    global plain_result
    for raw_key in data:
        if raw_key.find(DELETED) == 0:
            dict_result['-'].append(string + raw_key[len(DELETED):])
        elif raw_key.find(ADDED) == 0:
            dict_result['+'].append(string + raw_key[len(ADDED):])
        elif raw_key.find(CHANGED) == 0:
            if isinstance(data[raw_key], dict):
                render_plain_rec(
                    data[raw_key],
                    string + raw_key[len(CHANGED):] + '.'
                )
            else:
                dict_result['+/-'].append(string + raw_key[len(CHANGED):])
        else:
            if isinstance(data[raw_key], dict):
                render_plain_rec(
                    data[raw_key],
                    string + str(raw_key) + '.'
                )
