# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def remove_zeros(num):
    # Convert the number to a string to easily manipulate its digits
    num_str = str(num)
    
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over each character in the string
    for char in num_str:
        # If the character is not '0', add it to the result
        if char != '0':
            result += char
        # If the character is '0' and the result is not empty and the last character in the result is not '.', add it to the result
        elif result and result[-1] != '.':
            result += char
    
    # If the result is empty, return '0'
    if not result:
        return '0'
    
    # If the result ends with '.', remove it
    if result.endswith('.'):
        result = result[:-1]
    
    # Return the result
    return result