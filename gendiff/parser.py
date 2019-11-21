from gendiff.util import load_from_json_file


def gen_diff(path_to_file1, path_to_file2):
    data1 = load_from_json_file(path_to_file1)
    data2 = load_from_json_file(path_to_file2)
    result = "{" + '\n'
    result += parse_before(data1, data2)
    result += parse_after(data1, data2)
    result += '}'
    return result


def parse_before(data1, data2):
    result = ""
    for key in data1:
        slag = ''
        if key in data2:
            if data1[key] == data2[key]:
                slag += "    {}: {}\n".format(key, str(data1[key]))
            else:
                slag += "    - {}: {}\n".format(key, str(data1[key]))
                slag += "    + {}: {}\n".format(key, str(data2[key]))
        else:
            slag += "    - {}: {}\n".format(key, str(data1[key]))
        result += slag
    return result


def parse_after(data1, data2):
    result = ""
    for key in data2:
        slag = ''
        if key not in data1:
            slag += "    + {}: {}\n".format(key, str(data2[key]))
        result += slag
    return result
