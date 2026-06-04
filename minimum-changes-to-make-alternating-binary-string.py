def min_operations(s):
    # Initialize two counters for the number of operations needed to make the string alternating
    # starting with '0' and '1' respectively
    operations_starting_with_0 = 0
    operations_starting_with_1 = 0

    # Iterate over the string
    for i, char in enumerate(s):
        # If the character at the current index is not equal to the expected character in an alternating string
        # starting with '0', increment the operations counter for '0'
        if char != str(i % 2):
            operations_starting_with_0 += 1
        # If the character at the current index is not equal to the expected character in an alternating string
        # starting with '1', increment the operations counter for '1'
        if char != str((i + 1) % 2):
            operations_starting_with_1 += 1

    # Return the minimum number of operations needed to make the string alternating
    return min(operations_starting_with_0, operations_starting_with_1)