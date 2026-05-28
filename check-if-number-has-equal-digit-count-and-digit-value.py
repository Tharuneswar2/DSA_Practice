def digit_count(n):
    # Convert the number into a string to easily access each digit
    str_n = str(n)
    
    # Initialize a dictionary to store the count of each digit
    digit_dict = {}
    
    # Iterate over each character (digit) in the string
    for digit in str_n:
        # If the digit is already in the dictionary, increment its count
        if digit in digit_dict:
            digit_dict[digit] += 1
        # If the digit is not in the dictionary, add it with a count of 1
        else:
            digit_dict[digit] = 1
    
    # Iterate over each digit and its count in the dictionary
    for digit, count in digit_dict.items():
        # If the count of the digit is not equal to the digit's value, return False
        if int(digit) != count:
            return False
    
    # If the function hasn't returned False, all digit counts match their values, so return True
    return True

# Test the function
print(digit_count(1210))  # False
print(digit_count(2222))  # True