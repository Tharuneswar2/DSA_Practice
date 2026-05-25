def maxDiff(num):
    # Convert the number to a string to easily access each digit
    num_str = str(num)
    
    # Initialize the maximum difference and the digit to be replaced
    max_diff = 0
    replace_digit = None
    
    # Iterate over each digit in the number
    for digit in num_str:
        # If the digit is not 9, it can be replaced with 9 to maximize the difference
        if digit != '9':
            replace_digit = digit
            break
    
    # If a digit to be replaced is found, calculate the maximum difference
    if replace_digit is not None:
        # Replace the digit with 9 in the number string
        max_num_str = num_str.replace(replace_digit, '9')
        
        # Convert the modified number string back to an integer
        max_num = int(max_num_str)
        
        # Calculate the maximum difference
        max_diff = max_num - num
    
    return max_diff