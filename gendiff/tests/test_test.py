from gendiff.util import normalize_path
from gendiff.scripts.gendiff import gen_diff


def test_gen_dif():
    with_type('1.json')
    with_type('2.json')
    with_type('3.yml')
    with_type('4.json')


def with_type(file_type):
    path_to_file1 = normalize_path(
        'gendiff/tests/fixtures/test_before{}'.format(file_type)
        )
    path_to_file2 = normalize_path(
        'gendiff/tests/fixtures/test_after{}'.format(file_type)
        )
    if(file_type[0] == '4'):
        gen_dif_result = gen_diff(path_to_file1, path_to_file2, 'plain')
    else:
        gen_dif_result = gen_diff(path_to_file1, path_to_file2, 'json')
    f = open('gendiff/tests/fixtures/test_result_{}.txt'.format(file_type[0]))
    for line in f:
        assert gen_dif_result.find(line) >= 0
