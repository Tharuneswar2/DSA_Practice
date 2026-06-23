def faulty_keyboard(s, allowed):
    # Convert the allowed characters to a set for efficient lookups
    allowed_set = set(allowed)
    
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate over each character in the input string
    for char in s:
        # If the character is in the allowed set, add it to the result
        if char in allowed_set:
            result += char
    
    # Return the result
    return result

# Test the function
print(faulty_keyboard("abcpqr", "abc"))