def alternating_digit_sum(n):
    # Convert the number into a string to easily access each digit
    str_n = str(n)
    
    # Initialize the sum as 0
    total_sum = 0
    
    # Initialize a flag to track whether to add or subtract the current digit
    add = True
    
    # Iterate over each character (digit) in the string
    for digit in str_n:
        # Convert the character back into an integer
        int_digit = int(digit)
        
        # If add is True, add the digit to the sum; otherwise, subtract it
        if add:
            total_sum += int_digit
        else:
            total_sum -= int_digit
        
        # Flip the add flag for the next iteration
        add = not add
    
    # Return the final sum
    return total_sum