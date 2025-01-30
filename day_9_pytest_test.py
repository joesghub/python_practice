# Create a Python function that accepts a list of numbers and returns the sum. Write a test function using pytest to verify it works correctly. 

# Output Example:

# Sum of [1, 2, 3, 4, 5] is 15

# Pytest Output Example:

# Test results:
# Test passed: Sum of [1, 2, 3] is 6
# Test passed: Sum of [] is 0
# Test passed: Sum of [-1, -2, -3] is -6


# Asking for multiple space-separated values
# inputs = [i for i in input("Welcome to Add Them Up!\nIf you provide a list of numbers, I'll generate the sum for you!\nWhat numbers would you like to combine today?: ").split()]
# print(inputs)



############## VERSION 1 #############

# def summit():
#     # taking multiple inputs at a time separated by space and remooving extra spaces
#     inputs = [int(x) for x in input("Welcome to Add Them Up!\nIf you provide a list of numbers, I'll generate the sum for you!\nPlease add a space between each number for accurate results.\nWhat numbers would you like to combine today?: ").strip().split(" ")]
#     # print(inputs)

#     result = sum(inputs)
#     #print(f"Sum of {inputs} is {result}")


# def test_summit_6():
#     assert summit(1,2,3) == 6
# FAILED day_9_pytest_test.py::test_summit_6 - TypeError: summit() takes 0 positional arguments but 3 were given

# def test_summit_0():
#     assert summit( ) == 0
# FAILED day_9_pytest_test.py::test_summit_0 - OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

# def test_summit_negative_6():
#     assert summit(-1,-2,-3) == -6
#FAILED day_9_pytest_test.py::test_summit_negative_6 - TypeError: summit() takes 0 positional arguments but 3 were given


############## VERSION 2 #############

# def summit(inputs):
#     return sum(inputs)
# Remove the input() entirely from your code. The function should only sum a list that is passed to it.
# The function should accept a list of numbers as an argument, but currently, it takes user input inside the function.
# This prevents it from being reusable and makes testing unreliable.

# @pytest.fixture
# def example_data_6():
#     return [1, 2, 3]
#If you had a complex test setup, like needing to generate a large dataset dynamically, then a fixture might help.
# @pytest.fixture
# def large_numbers():
#     return list(range(1000))

# def test_large_summit(large_numbers):
#     assert summit(large_numbers) == sum(range(1000))
 

# def test_summit_6(example_data_6):
#     assert summit(example_data_6) == 6

# def test_summit_0():
#     assert summit( ) == 0

# def test_summit_negative_6():
#     assert summit(-1,-2,-3) == -6


############## VERSION 3 #############

import pytest

def summit(inputs):
    """Function to return the sum of a list of numbers"""
    return sum(inputs)

if __name__ == "__main__":
    inputs = [int(x) for x in input("Welcome to Add Them Up!\nIf you provide a list of numbers, I'll generate the sum for you!\nPlease add a space between each number for accurate results.\nWhat numbers would you like to combine today?: ").strip().split()]
    print(f"Sum of {inputs} is {summit(inputs)}")

def test_summit_6():
    assert summit([1,2,3]) == 6

def test_summit_0():
    assert summit([]) == 0

def test_summit_negative_6():
    assert summit([-1,-2,-3]) == -6


