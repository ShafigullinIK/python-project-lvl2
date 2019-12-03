from gendiff.util import ADDED, CHANGED, DELETED, DEVIDER


def render_plain(data):
    accum = render_plain_rec(data, "", [])
    return "\n".join(accum)


def render_plain_rec(data, string, accum):
    for raw_key in data:
        if raw_key.find(DELETED) == 0:
            accum.append("Property '{}{}' was removed".format(
                string, raw_key[len(DELETED):]
                )
            )
        elif raw_key.find(ADDED) == 0:
            if isinstance(data[raw_key], dict):
                accum.append(
                    "Property '{}{}' was added with value '{}'".format(
                        string,
                        raw_key[len(ADDED):],
                        'complex value'
                    )
                )
            else:
                accum.append(
                    "Property '{}{}' was added with value '{}'".format(
                        string,
                        raw_key[len(ADDED):],
                        data[raw_key]
                    )
                )
        elif raw_key.find(CHANGED) == 0:
            if isinstance(data[raw_key], dict):
                accum = render_plain_rec(
                    data[raw_key],
                    "{}{}.".format(string, raw_key[len(CHANGED):]),
                    accum
                )
            else:
                accum.append(
                    "Property '{}{}' was changed. From '{}' to '{}'".format(
                        string,
                        raw_key[len(CHANGED):],
                        str(data[raw_key]).split(DEVIDER)[0],
                        str(data[raw_key]).split(DEVIDER)[1]
                    )
                )
        else:
            if isinstance(data[raw_key], dict):
                accum = render_plain_rec(
                    data[raw_key],
                    "{}{}.".format(string, str(raw_key)),
                    accum
                )
    return accum
