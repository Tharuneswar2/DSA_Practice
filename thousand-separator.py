# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def thousandSeparator(n):
    # Convert the integer into a string to easily manipulate the digits
    str_n = str(n)
    
    # Initialize an empty string to store the result
    result = ""
    
    # Initialize a counter to keep track of the number of digits processed
    count = 0
    
    # Iterate over the string from right to left
    for i in range(len(str_n) - 1, -1, -1):
        # Add the current digit to the result
        result = str_n[i] + result
        
        # Increment the counter
        count += 1
        
        # If the counter is a multiple of 3 and not equal to the length of the string, add a comma
        if count % 3 == 0 and count != len(str_n):
            result = "," + result
    
    # Return the result
    return result