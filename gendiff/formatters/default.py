from gendiff.parsers import ADDED, CHANGED, DELETED, NORMAL


INDENT = "    "


def render_default(data):
    lines = render_rec(data, '', ["{"])
    result = "\n".join(lines)
    return result


def render_rec(data, indent, accum, level=1):
    for raw_key in data:
        pref = NORMAL
        if isinstance(raw_key, tuple):
            (pref, key) = raw_key
        else:
            key = raw_key
        if isinstance(data[raw_key], dict):
            if pref in (NORMAL, DELETED, ADDED):
                accum = add(
                    accum,
                    INDENT*level,
                    pref,
                    key,
                    data[raw_key],
                    render_rec,
                    level
                    )
            elif pref == CHANGED:
                (before, after) = data[raw_key]
                accum = add(
                    accum,
                    INDENT*level,
                    DELETED,
                    key,
                    before,
                    render_rec,
                    level
                    )
                accum = add(
                    accum,
                    INDENT*level,
                    ADDED,
                    key,
                    after,
                    render_rec, level
                    )
        else:
            if pref in (NORMAL, DELETED, ADDED):
                accum.append("{}    {}{}: {}".format(
                    indent, pref, key, str(data[raw_key])
                ))
            elif pref == CHANGED:
                (before, after) = data[raw_key]
                accum.append("{}    - {}: {}".format(
                    indent, key, before
                ))
                accum.append("{}    + {}: {}".format(
                    indent, key, after
                ))
    last_indent = INDENT*(level - 1)
    if level > 1:
        last_indent = "  {}".format(last_indent)
    accum.append("{}{}".format(last_indent, "}"))
    return accum


def add(accum, indent, sign, key, value, function, level):
    accum.append(
        "{}{}{}: {}".format(
                    indent, sign, key, "{"
                    )
                )
    return function(value, indent, accum, level+1)
