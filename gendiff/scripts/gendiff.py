import argparse
from gendiff.gendiff import gendiff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    gendiff(parser)


if __name__ == "__main__":
    main()
