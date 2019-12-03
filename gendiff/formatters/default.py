from gendiff.util import ADDED, CHANGED, DELETED, DEVIDER


def render_default(data):
    lines = render_rec(data, '', ["{"])
    result = "\n".join(lines)
    return result


def render_rec(data, indent, accum):
    for raw_key in data:
        key1 = ''
        key2 = ''
        if raw_key.find(DELETED) == 0:
            key1 = '- {}'.format(raw_key[len(DELETED):])
        elif raw_key.find(ADDED) == 0:
            key1 = '+ {}'.format(raw_key[len(ADDED):])
        elif raw_key.find(CHANGED) == 0:
            key1 = '- {}'.format(raw_key[len(CHANGED):])
            key2 = '+ {}'.format(raw_key[len(CHANGED):])
        if key1 == '':
            if isinstance(data[raw_key], dict):
                new_indent = '      {}'.format(indent)
                accum.append("{}{}: {}".format(
                    new_indent, raw_key, "{"
                    )
                )
                accum = render_rec(data[raw_key], new_indent, accum)
            else:
                accum.append("{}      {}: {}". format(
                    indent, raw_key, str(data[raw_key])
                    )
                )
        elif key2 == '':
            if isinstance(data[raw_key], dict):
                new_indent = '    {}'.format(indent)
                accum.append("{}{}: {}".format(
                    new_indent, key1, "{"
                    )
                )
                accum = render_rec(data[raw_key], new_indent, accum)
            else:
                accum.append("{}    {}: {}".format(
                    indent, key1, str(data[raw_key])
                ))
        else:
            if isinstance(data[raw_key], dict):
                new_indent = '    {}'.format(indent)
                accum.append("{}{}: {}". format(
                    new_indent, key1, "{"
                ))
                accum = render_rec(data[raw_key], new_indent, accum)
                accum.append("{}{}: {}". format(
                    new_indent, key2, "{"
                ))
                accum = render_rec(data[raw_key], new_indent, accum)
            else:
                first_value = str(data[raw_key]).split(DEVIDER)[0]
                second_value = str(data[raw_key]).split(DEVIDER)[1]
                accum.append("{}    {}: {}".format(
                    indent,
                    key1,
                    first_value
                    )
                )
                accum.append("{}    {}: {}".format(
                    indent,
                    key2,
                    second_value
                    )
                )
    accum.append("{}{}".format(indent, "}"))
    return accum
