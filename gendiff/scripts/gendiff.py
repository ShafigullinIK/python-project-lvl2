import argparse
from gendiff.parsers import gen_diff


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
    gen_diff_result = gen_diff(args.first_file, args.second_file)
    print(gen_diff_result)


if __name__ == "__main__":
    main()
