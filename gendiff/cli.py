import argparse


def init_argparser():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='First file name')
    parser.add_argument('second_file', type=str, help='second file name')
    parser.add_argument(
        '-f', '--format', type=str, help='set format of output'
        )
    return parser
