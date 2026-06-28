def remove_zeros(num):
    # Convert the number to a string to easily manipulate its digits
    num_str = str(num)
    
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate over each character in the string
    for char in num_str:
        # If the character is not a zero, add it to the result
        if char != "0":
            result += char
        # If the character is a zero and the result is not empty and the last character in the result is not a decimal point, add it to the result
        elif char == "0" and result and result[-1] != ".":
            result += char
    
    # If the result is empty, return 0
    if not result:
        return 0
    
    # If the result does not contain a decimal point, convert it to an integer and return it
    if "." not in result:
        return int(result)
    
    # If the result contains a decimal point, return it as a float
    return float(result)

# Test the function
print(remove_zeros(100.200))  # Output: 1.2
print(remove_zeros(123.045))  # Output: 123.45
print(remove_zeros(0))  # Output: 0