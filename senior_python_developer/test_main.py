import pytest
import json
from main import find_equal_sum_pairs, print_equal_sum_pairs, get_equal_sum_pairs_json

@pytest.fixture
def sample_data():
    arr = [1, 2, 4, 5, 6]
    expected_sum_to_pairs = [
        (6, [(1, 5), (2, 4)]),
        (7, [(1, 6), (2, 5)]),
    ]
    return arr, expected_sum_to_pairs

def test_find_equal_sum_pairs(sample_data):
    arr, expected = sample_data
    result = find_equal_sum_pairs(arr)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result == expected


def test_get_equal_sum_pairs_json(sample_data):
    _, expected = sample_data
    output = get_equal_sum_pairs_json(expected)
    parsed_output = json.loads(output)
    assert isinstance(parsed_output, list)
    assert len(parsed_output) == 2
    assert parsed_output == [
        {"sum": 6, "pairs": [[1, 5], [2, 4]]},
        {"sum": 7, "pairs": [[1, 6], [2, 5]]},
    ]
