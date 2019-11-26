from gendiff.util import normalize_path
from gendiff.scripts.gendiff import gen_diff


def test_gen_dif():
    with_type('json')
    #   with_type('yml')


def with_type(file_type):
    path_to_file1 = normalize_path(
        'gendiff/tests/fixtures/test_before1.{}'.format(file_type)
        )
    path_to_file2 = normalize_path(
        'gendiff/tests/fixtures/test_after1.{}'.format(file_type)
        )
    gen_dif_result = gen_diff(path_to_file1, path_to_file2)
    f = open('gendiff/tests/fixtures/test_result_{}1.txt'.format(file_type))
    for line in f:
        assert gen_dif_result.find(line) >= 0
