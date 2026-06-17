def clear_digits(n):
    # Convert the number to a string to easily access each digit
    str_n = str(n)
    
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over each character (digit) in the string
    for char in str_n:
        # If the digit is not '0', add it to the result
        if char != '0':
            result += char
    
    # If the result is empty (i.e., the input number was 0), return 0
    if result == '':
        return 0
    # Otherwise, convert the result back to an integer and return it
    else:
        return int(result)

# Test the function
print(clear_digits(100))  # Output: 1
print(clear_digits(101))  # Output: 11
print(clear_digits(102))  # Output: 12
print(clear_digits(103))  # Output: 13
print(clear_digits(104))  # Output: 14
print(clear_digits(105))  # Output: 15
print(clear_digits(106))  # Output: 16
print(clear_digits(107))  # Output: 17
print(clear_digits(108))  # Output: 18
print(clear_digits(109))  # Output: 19
print(clear_digits(110))  # Output: 11