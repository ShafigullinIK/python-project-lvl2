from gendiff.util import load_from_file


DELETED = ' deleted '
ADDED = ' added '
CHANGED = ' changed '
DEVIDER = "~|~"


def gen_diff(path_to_file1, path_to_file2):
    data1 = load_from_file(path_to_file1)
    data2 = load_from_file(path_to_file2)
    result = iter(data1, data2)
    return render(result)


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


def render(data):
    return render_rec(data, '')


def render_rec(data, indent):
    result = "{" + '\n'
    for raw_key in data:
        key1 = ''
        key2 = ''
        if raw_key.find(DELETED) == 0:
            key1 = '- ' + raw_key[len(DELETED):]
        elif raw_key.find(ADDED) == 0:
            key1 = '+ ' + raw_key[len(ADDED):]
        elif raw_key.find(CHANGED) == 0:
            key1 = '- ' + raw_key[len(CHANGED):]
            key2 = '+ ' + raw_key[len(CHANGED):]
        if key1 == '':
            if isinstance(data[raw_key], dict):
                new_indent = '      ' + indent
                result += new_indent + raw_key + ': ' +\
                    render_rec(data[raw_key], new_indent)
            else:
                result += indent +\
                    "      {}: {}\n".format(raw_key, str(data[raw_key]))
        elif key2 == '':
            if isinstance(data[raw_key], dict):
                new_indent = '    ' + indent
                result += new_indent + key1 +\
                    ': ' + render_rec(data[raw_key], new_indent)
            else:
                result += indent +\
                    "    {}: {}\n".format(key1, str(data[raw_key]))
        else:
            if isinstance(data[raw_key], dict):
                new_indent = '    ' + indent
                result += new_indent + key1 +\
                    ': ' + render_rec(data[raw_key], new_indent)
                result += new_indent + key2 +\
                    ': ' + render_rec(data[raw_key], new_indent)
            else:
                first_value = str(data[raw_key]).split(DEVIDER)[0]
                second_value = str(data[raw_key]).split(DEVIDER)[1]
                result += indent + "    {}: {}\n".format(key1, first_value)
                result += indent + "    {}: {}\n".format(key2, second_value)
    result += indent + '}' + '\n'
    return result
