# python-debugging-ai-practical

Python debugging, unit testing, and AI-assisted code review practical.

This project contains three small utility functions in `debug_practice.py`. The original implementations included three intentional bugs. Those bugs have been corrected, and `test_debug_practice.py` verifies the expected behavior with Python's built-in `unittest` framework.

## Functions

| Function | Purpose |
|---|---|
| `calculate_average(numbers)` | Returns the arithmetic mean of a numeric sequence. |
| `is_even(number)` | Returns `True` if `number` is even, otherwise `False`. |
| `find_maximum(numbers)` | Returns the largest value in a non-empty sequence. |

## Bugs fixed

1. **`calculate_average` — undefined name.** The function called `len(number)` instead of `len(numbers)`, which raised `NameError`. It now divides the sum by `len(numbers)`.
2. **`is_even` — inverted parity check.** The condition `number % 2 == 1` identified odd numbers. It now uses `number % 2 == 0`.
3. **`find_maximum` — wrong seed and comparison.** `maximum` started at `0` (incorrect for all-negative lists) and the loop used `<`, which tracked a minimum. It now seeds from `numbers[0]` and updates when `number > maximum`.

## Test coverage

`test_debug_practice.py` includes 16 tests covering typical inputs and edge cases:

- **`calculate_average`:** positive integers, mixed values, a single value, negatives, and an empty list (`ZeroDivisionError`).
- **`is_even`:** even and odd positives, zero, and even/odd negatives.
- **`find_maximum`:** positive integers, a single value, all-negative lists, mixed signs, duplicates, and an empty list (`IndexError`).

## Running tests

From the project root:

```bash
python -m unittest -v
```
