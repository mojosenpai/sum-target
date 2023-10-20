# Sum Target
Problem definition: given a space-separated list of numbers in a file, find all pairs of numbers that add up to a given target number.
# Solution
Traverse the list once. Keep all seen numbers in a hash table and for each number `x`, check whether `target - x` is in the hash table.
# Complexity
``Time Complexity: O(n)``

``Space Complexity: O(n)``

# How to run
The only dependency of the project is `pytest`. You can install it by running `pip install pytest` in the terminal. You can also run the tests py running `pytest test_sum_target` in the terminal.