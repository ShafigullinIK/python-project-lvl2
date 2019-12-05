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
        inner = data[raw_key]
        if 'value' in inner:
            if pref in (NORMAL, DELETED, ADDED):
                accum.append("{}    {}{}: {}".format(
                    indent, pref, key, inner['value']
                ))
            elif pref == CHANGED:
                (before, after) = inner['value']
                accum.append("{}    - {}: {}".format(
                    indent, key, before
                ))
                accum.append("{}    + {}: {}".format(
                    indent, key, after
                ))
        else:
            if pref in (NORMAL, DELETED, ADDED):
                accum = add(
                    accum,
                    INDENT*level,
                    pref,
                    key,
                    inner,
                    render_rec,
                    level
                    )
            elif pref == CHANGED:
                (before, after) = inner
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
