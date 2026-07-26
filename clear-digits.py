# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def clear_digits(num):
    # Convert the number to a string to easily access each digit
    num_str = str(num)
    
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over each character (digit) in the string
    for digit in num_str:
        # If the digit is not '0', add it to the result
        if digit != '0':
            result += digit
    
    # If the result is empty (i.e., the input number was 0), return 0
    if result == '':
        return 0
    
    # Convert the result back to an integer and return it
    return int(result)