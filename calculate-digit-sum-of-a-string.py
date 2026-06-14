def digit_sum(s):
    # Initialize a variable to store the sum of digits
    total_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a digit
        if char.isdigit():
            # Add the digit to the total sum
            total_sum += int(char)
    
    # Return the total sum
    return total_sum

# Test the function
print(digit_sum("abc123"))  # Output: 6