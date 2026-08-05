# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def min_operations(nums):
    # Initialize variables to store the minimum operations required for each remainder
    remainder_1 = float('inf')  # Initialize with positive infinity
    remainder_2 = float('inf')  # Initialize with positive infinity

    # Iterate over each number in the list
    for num in nums:
        # Calculate the remainder when the number is divided by 3
        remainder = num % 3
        
        # If the remainder is 1, update the minimum operations required for remainder 1
        if remainder == 1:
            remainder_1 = min(remainder_1, 1)  # We need at least 1 operation to make it divisible by 3
        # If the remainder is 2, update the minimum operations required for remainder 2
        elif remainder == 2:
            remainder_2 = min(remainder_2, 1)  # We need at least 1 operation to make it divisible by 3

    # Calculate the minimum operations required to make all elements divisible by 3
    # We need to make all elements with remainder 1 or 2 divisible by 3
    min_ops = min(remainder_1 + remainder_2, 2)  # We can make all elements divisible by 3 in at most 2 operations

    return min_ops