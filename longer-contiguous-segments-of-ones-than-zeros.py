def check_zero_ones(s):
    max_ones = max_zeros = 0
    curr_ones = curr_zeros = 0

    # Iterate over the string
    for char in s:
        # If the character is '1', increment the current ones count
        if char == '1':
            curr_ones += 1
            # Reset the current zeros count
            curr_zeros = 0
        # If the character is '0', increment the current zeros count
        else:
            curr_zeros += 1
            # Reset the current ones count
            curr_ones = 0
        
        # Update the maximum ones and zeros counts
        max_ones = max(max_ones, curr_ones)
        max_zeros = max(max_zeros, curr_zeros)

    # Return True if the maximum ones count is greater than the maximum zeros count
    return max_ones > max_zeros