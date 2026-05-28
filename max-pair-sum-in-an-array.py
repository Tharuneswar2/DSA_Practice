def max_pair_sum(arr):
    # Check if the array has less than 2 elements
    if len(arr) < 2:
        return None

    # Initialize max1 and max2 as negative infinity
    max1 = max2 = float('-inf')

    # Iterate through the array to find the maximum and second maximum elements
    for num in arr:
        # If the current number is greater than max1, update max1 and max2
        if num > max1:
            max2 = max1
            max1 = num
        # If the current number is less than max1 but greater than max2, update max2
        elif num > max2 and num != max1:
            max2 = num

    # Return the sum of max1 and max2
    return max1 + max2

# Test the function
print(max_pair_sum([1, 2, 3, 4, 5]))  # Output: 9
print(max_pair_sum([-1, -2, -3, -4, -5]))  # Output: -3