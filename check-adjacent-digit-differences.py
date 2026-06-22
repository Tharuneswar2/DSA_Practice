def check_adjacent_digit_differences(num):
    # Convert the number to a string to easily access each digit
    num_str = str(num)
    
    # Initialize a flag to track if the number has adjacent digit differences
    has_adjacent_digit_differences = False
    
    # Iterate over the digits in the number
    for i in range(len(num_str) - 1):
        # Check if the current digit is one more than the next digit
        if int(num_str[i]) == int(num_str[i + 1]) + 1:
            # If it is, set the flag to True
            has_adjacent_digit_differences = True
            # Break out of the loop since we've found a pair of adjacent digits with a difference of 1
            break
    
    # Return the result
    return has_adjacent_digit_differences

# Test the function
print(check_adjacent_digit_differences(123))  # True
print(check_adjacent_digit_differences(124))  # False