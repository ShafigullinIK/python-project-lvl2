from gendiff.util import ADDED, CHANGED, DELETED, DEVIDER


plain_result = ''


def render_plain(data):
    render_plain_rec(data, "")
    return plain_result


def render_plain_rec(data, string):
    global plain_result
    for raw_key in data:
        if raw_key.find(DELETED) == 0:
            plain_result += "Property '{}' was removed\n".format(
                string + raw_key[len(DELETED):]
                )
        elif raw_key.find(ADDED) == 0:
            if isinstance(data[raw_key], dict):
                plain_result += "Property '{}' was added with value\
 '{}'\n".format(
                    string + raw_key[len(ADDED):],
                    'complex value'
                )
            else:
                plain_result += "Property '{}' was added\
 with value '{}'\n".format(
                    string + raw_key[len(ADDED):],
                    data[raw_key]
                )
        elif raw_key.find(CHANGED) == 0:
            if isinstance(data[raw_key], dict):
                render_plain_rec(
                    data[raw_key],
                    string + raw_key[len(CHANGED):] + '.'
                )
            else:
                plain_result += "Property '{}' was changed.\
 From '{}' to '{}'\n".format(
                    string + raw_key[len(CHANGED):],
                    str(data[raw_key]).split(DEVIDER)[0],
                    str(data[raw_key]).split(DEVIDER)[1]
                )
        else:
            if isinstance(data[raw_key], dict):
                render_plain_rec(
                    data[raw_key],
                    string + str(raw_key) + '.'
                )
