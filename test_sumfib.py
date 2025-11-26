# test_fibonacci.py

import pytest
from sumfib import fibonacci_sum   

def test_fibonacci_sum():
    # Sample test data
    n = 5

    # Expected result
    # Fibonacci series: 0, 1, 1, 2, 3 → Sum = 7
    expected_sum = 7

    # Function call
    result = fibonacci_sum(n)

    # Assertion
    assert result == expected_sum