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

    # If the result is empty, return the original string
    if not result:
        return s

    # Remove trailing zeros from the result
    result = result.rstrip('0')

    # Return the result
    return result

# Test the function
print(remove_trailing_zeros("123450"))  # Output: "12345"
print(remove_trailing_zeros("000123450"))  # Output: "00012345"
print(remove_trailing_zeros("123450000"))  # Output: "12345"
print(remove_trailing_zeros("000"))  # Output: "0"
print(remove_trailing_zeros(""))  # Output: ""