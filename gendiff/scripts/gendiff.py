import argparse
import json
import os.path


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='First file name')
    parser.add_argument('second_file', type=str, help='second file name')
    parser.add_argument(
        '-f', '--format',
        type=str,
        help='set format of output'
    )
    args = parser.parse_args()
    gen_diff(args.first_file, args.second_file)


def gen_diff(path_to_file1, path_to_file2):
    file1 = normalize_path(path_to_file1)
    file2 = normalize_path(path_to_file2)
    data1 = json.load(open(file1))
    data2 = json.load(open(file2))
    space = "    "
    result = "{" + '\n'
    for key in data1:
        slag = ''
        if key in data2:
            if data1[key] == data2[key]:
                slag += space + key + ': ' + str(data1[key]) + '\n'
            else:
                slag += space + '- ' + key + ': ' + str(data1[key]) + '\n'
                slag += space + '+ ' + key + ': ' + str(data2[key]) + '\n'
        else:
            slag += space + '- ' + key + ': ' + str(data1[key]) + '\n'
        result += slag
    for key in data2:
        slag = ''
        if key not in data1:
            slag += space + '+ ' + key + ': ' + str(data2[key]) + '\n'
        result += slag
    result += '}'
    print(result)


def normalize_path(path_to_file):
    return os.path.abspath(path_to_file)


if __name__ == "__main__":
    main()
