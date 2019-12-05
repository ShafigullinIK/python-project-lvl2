from gendiff.parsers import ADDED, CHANGED, DELETED, NORMAL


def render_plain(data):
    accum = render_plain_rec(data, "", [])
    return "\n".join(accum)


def render_plain_rec(data, string, accum):
    for raw_key in data:
        (pref, key) = raw_key
        inner = data[raw_key]
        if pref == DELETED:
            accum.append("Property '{}{}' was removed".format(
                string, key
                )
            )
        elif pref == ADDED:
            if 'value' not in inner:
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
                        inner['value']
                    )
                )
        elif pref == CHANGED:
            if 'value' not in inner:
                accum = render_plain_rec(
                    inner,
                    "{}{}.".format(string, key),
                    accum
                )
            else:
                (before, after) = inner['value']
                accum.append(
                    "Property '{}{}' was changed. From '{}' to '{}'".format(
                        string,
                        key,
                        before,
                        after
                    )
                )
        elif pref == NORMAL:
            if 'value' not in inner:
                accum = render_plain_rec(
                    inner,
                    "{}{}.".format(string, str(key)),
                    accum
                )
    return accum
