# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def add_two_integers(a, b):
    # We don't need to do any error checking here because the problem statement assumes that the inputs are integers
    # We can simply add the two integers together using the built-in '+' operator
    # This operation has a time complexity of O(1) because it only involves a single operation
    return a + b

# Test the function with some example inputs
print(add_two_integers(1, 2))  # Output: 3
print(add_two_integers(-1, 1))  # Output: 0
print(add_two_integers(-1, -1))  # Output: -2