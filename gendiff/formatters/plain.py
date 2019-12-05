from gendiff.parsers import ADDED, CHANGED, DELETED, NORMAL


def render_plain(data):
    accum = render_plain_rec(data, "", [])
    return "\n".join(accum)


def render_plain_rec(data, string, accum):
    for raw_key in data:
        (pref, key) = raw_key
        if pref == DELETED:
            accum.append("Property '{}{}' was removed".format(
                string, key
                )
            )
        elif pref == ADDED:
            if isinstance(data[raw_key], dict):
                accum.append(
                    "Property '{}{}' was added with value '{}'".format(
                        string,
                        key,
                        'complex value'
                    )
                )
            else:
                accum.append(
                    "Property '{}{}' was added with value '{}'".format(
                        string,
                        key,
                        data[raw_key]
                    )
                )
        elif pref == CHANGED:
            if isinstance(data[raw_key], dict):
                accum = render_plain_rec(
                    data[raw_key],
                    "{}{}.".format(string, key),
                    accum
                )
            else:
                (before, after) = data[raw_key]
                accum.append(
                    "Property '{}{}' was changed. From '{}' to '{}'".format(
                        string,
                        key,
                        before,
                        after
                    )
                )
        elif pref == NORMAL:
            if isinstance(data[raw_key], dict):
                accum = render_plain_rec(
                    data[raw_key],
                    "{}{}.".format(string, str(key)),
                    accum
                )
    return accum
