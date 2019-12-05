DELETED = '- '
ADDED = '+ '
CHANGED = ' changed '
NORMAL = '  '


def prepare_data(data1, data2):
    d = {}
    for key in data1.keys() & data2.keys():
        if data1[key] == data2[key]:
            d[(NORMAL, key)] = data1[key]
        elif isinstance(data1[key], dict):
            d[(NORMAL, key)] = prepare_data(data1[key], data2[key])
        else:
            d[(CHANGED, key)] = (data1[key], data2[key])
    for key in data1.keys() - data2.keys():
        d[(DELETED, key)] = data1[key]
    for key in data2.keys() - data1.keys():
        d[(ADDED, key)] = data2[key]
    return d
