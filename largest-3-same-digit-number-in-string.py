# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def largestGoodInteger(num: str) -> str:
    # Initialize an empty string to store the result
    result = ""
    
    # Initialize a variable to store the maximum length of the same digit substring
    max_length = 0
    
    # Initialize a variable to store the current digit
    current_digit = ""
    
    # Initialize a variable to store the count of the current digit
    current_count = 0
    
    # Iterate over the input string
    for digit in num:
        # If the current digit is the same as the previous digit, increment the count
        if digit == current_digit:
            current_count += 1
        # If the current digit is different from the previous digit, reset the count
        else:
            current_digit = digit
            current_count = 1
        
        # If the count of the current digit is 3 and it's greater than the max_length, update the result and max_length
        if current_count == 3 and int(digit) > int(result) if result else True:
            result = digit * 3
            max_length = 3
    
    # Return the result
    return result