def find_closest_to_zero(numbers):
    # Initialize the minimum difference and the closest number to zero
    min_diff = float('inf')  # Initialize with positive infinity
    closest_num = None

    # Iterate over each number in the list
    for num in numbers:
        # Calculate the absolute difference between the current number and zero
        diff = abs(num)

        # If the difference is less than the current minimum difference
        if diff < min_diff:
            # Update the minimum difference and the closest number to zero
            min_diff = diff
            closest_num = num

    # Return the closest number to zero
    return closest_num

# Example usage:
numbers = [10, -5, 3, 7, -1]
print(find_closest_to_zero(numbers))  # Output: -1