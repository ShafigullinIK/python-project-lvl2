DELETED = '- '
ADDED = '+ '
CHANGED = ' changed '
NORMAL = '  '


def prepare_data(data1, data2):
    d = {}
    for key in data1.keys() & data2.keys():
        if isinstance(data1[key], dict):
            d[(NORMAL, key)] = prepare_data(data1[key], data2[key])
        elif data1[key] == data2[key]:
            d[(NORMAL, key)] = {'value': data1[key]}
        else:
            d[(CHANGED, key)] = {'value': (data1[key], data2[key])}
    for key in data1.keys() - data2.keys():
        if isinstance(data1[key], dict):
            d[(DELETED, key)] = put_value(data1[key])
        else:
            d[(DELETED, key)] = {'value': data1[key]}
    for key in data2.keys() - data1.keys():
        if isinstance(data2[key], dict):
            d[(ADDED, key)] = put_value(data2[key])
        else:
            d[(ADDED, key)] = {'value': data2[key]}
    return d


def put_value(source):
    d = {}
    for key in source.keys():
        inner = source[key]
        if isinstance(inner, dict):
            d[(NORMAL, key)] = put_value(inner)
        else:
            d[(NORMAL, key)] = {'value': inner}
    return d
