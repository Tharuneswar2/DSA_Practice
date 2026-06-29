def min_operations(nums):
    # Initialize variables to store the count of elements with remainder 0, 1, and 2 when divided by 3
    remainder_0 = 0
    remainder_1 = 0
    remainder_2 = 0

    # Iterate through the list of numbers
    for num in nums:
        # Calculate the remainder when the number is divided by 3
        remainder = num % 3
        
        # Increment the count of elements with the calculated remainder
        if remainder == 0:
            remainder_0 += 1
        elif remainder == 1:
            remainder_1 += 1
        else:
            remainder_2 += 1

    # The minimum number of operations is the minimum between the count of elements with remainder 1 and 2
    # This is because we can always make an element with remainder 1 or 2 divisible by 3 by adding 2 or 1 respectively
    # However, we can also make an element with remainder 1 or 2 divisible by 3 by subtracting 1 or 2 respectively
    # Therefore, we need to consider the minimum between the two counts
    min_ops = min(remainder_1, remainder_2)

    # If the count of elements with remainder 1 is greater than the count of elements with remainder 2
    # We can make the extra elements with remainder 1 divisible by 3 by adding 2 to each of them
    # This requires an additional operation for each extra element
    if remainder_1 > remainder_2:
        min_ops += remainder_1 - remainder_2

    # If the count of elements with remainder 2 is greater than the count of elements with remainder 1
    # We can make the extra elements with remainder 2 divisible by 3 by subtracting 1 from each of them
    # This requires an additional operation for each extra element
    elif remainder_2 > remainder_1:
        min_ops += remainder_2 - remainder_1

    # Return the minimum number of operations
    return min_ops

# Example usage:
nums = [1, 2, 3, 4, 5, 6]
print(min_operations(nums))