from gendiff.util import load_from_file, ADDED, CHANGED, DELETED, DEVIDER
from gendiff import formatters


def gen_diff(path_to_file1, path_to_file2, formatter):
    data1 = load_from_file(path_to_file1)
    data2 = load_from_file(path_to_file2)
    result = iter(data1, data2)
    if formatter == 'plain':
        return formatters.render_plain(result)
    elif formatter == 'json':
        return formatters.render_json(result)
    else:
        return formatters.render_default(result)


def iter(data1, data2):
    d = {}
    for key in data1.keys() & data2.keys():
        if data1[key] == data2[key]:
            d[key] = data1[key]
        elif isinstance(data1[key], dict):
            d[key] = iter(data1[key], data2[key])
        else:
            d[CHANGED + key] = str(data1[key]) + DEVIDER + str(data2[key])
    for key in data1.keys() - data2.keys():
        d[DELETED + key] = data1[key]
    for key in data2.keys() - data1.keys():
        d[ADDED + key] = data2[key]
    return d
