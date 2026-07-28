# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def find_closest_to_zero(numbers):
    # Initialize the minimum difference and the closest number to zero
    # We assume the first number in the list is the closest to zero initially
    min_diff = abs(numbers[0])  # Calculate the absolute difference of the first number
    closest_num = numbers[0]  # Store the first number as the closest to zero

    # Iterate through the list of numbers starting from the second number
    for num in numbers[1:]:
        # Calculate the absolute difference of the current number
        diff = abs(num)
        
        # If the difference of the current number is less than the minimum difference found so far
        if diff < min_diff:
            # Update the minimum difference and the closest number to zero
            min_diff = diff
            closest_num = num

    # Return the closest number to zero
    return closest_num