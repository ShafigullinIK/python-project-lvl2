import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='First file name')
    parser.add_argument('second_file', type=str, help='second file name')
    args = parser.parse_args()
    print(args.first_file)


if __name__ == "__main__":
    main()
