from gendiff.util import normalize_path
from gendiff.scripts.gendiff import gen_diff


def test_gen_dif():
    path_to_file1 = normalize_path('gendiff/tests/fixtures/test_before.json')
    path_to_file2 = normalize_path('gendiff/tests/fixtures/test_after.json')
    gen_dif_result = gen_diff(path_to_file1, path_to_file2)
    f = open('gendiff/tests/fixtures/test_result.txt')
    correct_result = f.read()
    assert correct_result == gen_dif_result
