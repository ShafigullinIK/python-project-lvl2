from gendiff.util import load_from_json_file


def gen_diff(path_to_file1, path_to_file2):
    data1 = load_from_json_file(path_to_file1)
    data2 = load_from_json_file(path_to_file2)
    space = "    "
    result = "{" + '\n'
    for key in data1:
        slag = ''
        if key in data2:
            if data1[key] == data2[key]:
                slag += space + key + ': ' + str(data1[key]) + '\n'
            else:
                slag += space + '- ' + key + ': ' + str(data1[key]) + '\n'
                slag += space + '+ ' + key + ': ' + str(data2[key]) + '\n'
        else:
            slag += space + '- ' + key + ': ' + str(data1[key]) + '\n'
        result += slag
    for key in data2:
        slag = ''
        if key not in data1:
            slag += space + '+ ' + key + ': ' + str(data2[key]) + '\n'
        result += slag
    result += '}'
    return result
