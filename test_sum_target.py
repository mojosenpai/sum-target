import pytest

from sum_target import parse_text

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
