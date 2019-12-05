from gendiff.formatters.default import render_default
from gendiff.formatters.json import render_json
from gendiff.formatters.plain import render_plain
from gendiff.parsers import prepare_data
from gendiff.util import load_from_file
from gendiff.cli import init_argparser


def gendiff():
    parser = init_argparser()
    args = parser.parse_args()
    gen_diff_result = gen_diff(
        args.first_file,
        args.second_file,
        args.format
    )
    print(gen_diff_result)


def gen_diff(path_to_file1, path_to_file2, formatter):
    data1 = load_from_file(path_to_file1)
    data2 = load_from_file(path_to_file2)
    result = prepare_data(data1, data2)
    f = render_default
    if formatter == 'plain':
        f = render_plain
    elif formatter == 'json':
        f = render_json
    return f(result)
