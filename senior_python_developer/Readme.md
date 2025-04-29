# Equal Sum Pairs Assignment

## Task Description
Given an unsorted array of integers `A[]`, the task was to **find and print all unique pairs** in the array that have the **same sum**, and then **group those pairs by their sum**. The output must:

- Include **only** those sums that have **at least two different pairs** associated with them.
- Be printed in the following format:
  ```
  Pairs: (a, b) (c, d) have sum X
  ```
- The pairs and their corresponding sums should be **sorted by the sum in ascending order**.

### Example Input:
```python
A = [6, 4, 12, 10, 22, 54, 32, 42, 21, 11]
```

### Example Output:
```
Pairs: (4, 12) (6, 10) have sum 16
Pairs: (10, 22) (11, 21) have sum 32
... and so on
```

---

## My Solution

I built a modular Python script with the following components:

### 1. `find_equal_sum_pairs(arr)`
- Generates all unique unordered pairs in the input array using `itertools.combinations`.
- Groups them by their sum using a `defaultdict(list)`.
- Filters out any sums that don’t have **at least two pairs**.
- Returns the result as a **sorted list** of tuples: `(sum, list_of_pairs)`.

### 2. `print_equal_sum_pairs(sum_to_pairs)`
- Formats the grouped pairs into strings and prints them directly.
- Each line follows the required output format: `Pairs: (a, b) (c, d) have sum X`
- Pairs are joined inline per sum group.

### 3. `get_equal_sum_pairs_json(sum_to_pairs)`
- Converts the result into a JSON-serializable format.
- Each item includes the sum and a list of pair tuples.
- Useful for exporting results to for instance APIs.

---

## Thought Process

### Step-by-step Reasoning:
1. 
    I used `itertools.combinations(arr, 2)` to generate every pair in the array. This avoids using nested loops and keeps the code clean and efficient.

2. 
    I used a `defaultdict(list)` to collect pairs under their respective sums.

3. 
    I then filtered the dictionary to only include sums with at least two pairs, and sorted them to match the output requirement.

4. 
    I split the solution into multiple functions: one for finding pairs, one for printing, and one for exporting. This follows the Single Responsibility Principle and makes it easy to test and adapt.

5.
    I inlcuded a JSON export function, to prepare for integration with APIs


## Bonus: Testing
As a bonus, I added a test suite using `pytest` to validate the core functionality:

- Tested that the `find_equal_sum_pairs` function returns the correct grouped sums.
- Checked that the JSON formatting returns valid structured data.

This makes the project easier to extend and ensures correctness when refactoring.
