# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def remove_trailing_zeros(s):
    # Check if the input string is empty
    if not s:
        return s
    
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate over the input string from right to left
    for char in reversed(s):
        # If the character is not a zero, add it to the result and break the loop
        if char != '0':
            result = char + result
            break
        # If the character is a zero, add it to the result
        else:
            result = char + result
    
    # If the result is empty or only contains zeros, return '0'
    if result == "" or (len(result) == 1 and result[0] == '0'):
        return '0'
    
    # Remove trailing zeros from the result
    result = result.rstrip('0')
    
    # Return the result
    return result