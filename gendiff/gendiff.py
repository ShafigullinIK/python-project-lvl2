from gendiff.formatters.default import render_default
from gendiff.formatters.json import render_json
from gendiff.formatters.plain import render_plain
from gendiff.parsers import prepare_data
from gendiff.util import load_from_file


def gendiff(parser):
    parser.add_argument('first_file', type=str, help='First file name')
    parser.add_argument('second_file', type=str, help='second file name')
    parser.add_argument(
        '-f', '--format',
        type=str,
        help='set format of output'
    )
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
