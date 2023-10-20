import pytest

from sum_target import parse_text, find_all_pairs_with_sum_target

@pytest.mark.parametrize('nums, target, expected_pairs',
                         [
                             (
                                     [], 1, []
                             ),
                             (
                                     [2, 5], 7, [[5, 2]]
                             ),
                             (
                                     [3], 6, []
                             ),
                             (
                                     [3, 2, 3], 6, [[3, 3]]
                             ),
                             (
                                     [2, 3, 4, 5, 6], 9, [[5, 4], [6, 3]]
                             ),
                             (
                                     [2, 3, 4, 5, 6], 9, [[3, 6], [5, 4]]
                             ),
                             (
                                     [2, 5, 1, 7, 5], 4, []
                             ),
                             (
                                 [2, 3, -1], 2, [[3, -1]]
                             )
                         ])
def test_find_all_pairs_with_sum_target(nums, target, expected_pairs):
    actual_pairs = [i.sort() for i in find_all_pairs_with_sum_target(nums, target)]
    sorted_expected_pairs = [i.sort() for i in expected_pairs]
    assert actual_pairs == sorted_expected_pairs

@pytest.mark.parametrize('file_content, expected_list', [
    (
        '', []
    ),
    (
        '1 4 2 6 1', [1, 4, 2, 6, 1]
    ),
    ('5 2 -1', [5, 2, -1])
])
def test_parse_text(file_content, expected_list):
    assert parse_text(file_content) == expected_list


@pytest.mark.parametrize('value', [
    'omae wa mou shindeiru',
    '5 2 --1'
])
def test_parse_text_invalid_input(value):
    with pytest.raises(ValueError) as excinfo:
        parse_text(value)
    assert 'input file must only contain integers separated by space' in str(excinfo.value)
