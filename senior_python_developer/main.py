from itertools import combinations
from collections import defaultdict
import json

def find_equal_sum_pairs(arr: list) -> list:
    """
    Finds all pairs of numbers in the array that have the same sum and
    groups them by the sum
    """
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        raise ValueError("Input must be a list of integers.")
    if len(arr) < 2:
        raise ValueError("Input array must contain at least two elements.")
    
    sum_to_pairs = defaultdict(list)
    for a, b in combinations(arr, 2):
        pair = (a, b)
        sum_to_pairs[a+b].append(pair)

    filtered_sums = ((s, pairs) for s, pairs in sum_to_pairs.items() if len(pairs)>=2)
    sorted_sum_to_pairs = sorted(filtered_sums, key=lambda x:x[0])

    return sorted_sum_to_pairs

def print_equal_sum_pairs(sum_to_pairs: list) -> None:
    """
    Prints the pairs of numbers that have the same sum
    """
    if not isinstance(sum_to_pairs, list):
        raise ValueError("Input must be a list of (sum, list_of_pairs) tuples.")
    
    for s, pairs in sum_to_pairs:
        pair_strings = " ".join(f'{pair}' for pair in pairs )
        print(f'Pairs: {pair_strings} have sum {s}')

def get_equal_sum_pairs_json(sum_to_pairs: list) -> list:
    """
    Returns the pairs of numbers that have the same sum in JSON format
    """
    if not isinstance(sum_to_pairs, list):
        raise ValueError("Input must be a list of (sum, list_of_pairs) tuples.")
    
    result = [{'sum': s, 'pairs': [pair for pair in pairs]} for s, pairs in sum_to_pairs]
    try:
        return json.dumps(result, indent=4)
    except TypeError as e:
        raise ValueError(f"Error converting to JSON: {e}")


if __name__ == "__main__":

    A =[6, 4, 12, 10, 22, 54, 32, 42, 21, 11]
    sum_to_pairs = find_equal_sum_pairs(A)
    print_equal_sum_pairs(sum_to_pairs)
    A = [4, 23, 65, 67, 24, 12, 86]
    sum_to_pairs = find_equal_sum_pairs(A)
    print_equal_sum_pairs(sum_to_pairs)
    print(get_equal_sum_pairs_json(sum_to_pairs))
