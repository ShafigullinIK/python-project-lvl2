from gendiff.gendiff import gen_diff
import os.path


def test_gen_dif():
    with_type('1.json')
    with_type('2.json')
    with_type('3.yml')
    with_type('4.json')
    with_type('5.json')


def with_type(file_type):
    path_to_file1 = os.path.abspath(
        'tests/fixtures/test_before{}'.format(file_type)
        )
    path_to_file2 = os.path.abspath(
        'tests/fixtures/test_after{}'.format(file_type)
        )
    if file_type[0] == '4':
        gen_dif_result = gen_diff(path_to_file1, path_to_file2, 'plain')
    elif file_type[0] == '5':
        gen_dif_result = gen_diff(path_to_file1, path_to_file2, 'json')
    else:
        gen_dif_result = gen_diff(path_to_file1, path_to_file2, 'default')
    f = open('tests/fixtures/test_result_{}.txt'.format(file_type[0]))
    for line in f:
        assert gen_dif_result.find(line) >= 0
