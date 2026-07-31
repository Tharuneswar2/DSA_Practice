# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def split_string(s, sep):
    # Initialize an empty list to store the result
    result = []
    
    # Initialize an empty string to store the current substring
    current_substring = ""
    
    # Iterate over each character in the input string
    for char in s:
        # If the character is the separator, add the current substring to the result and reset it
        if char == sep:
            # Add the current substring to the result
            result.append(current_substring)
            # Reset the current substring
            current_substring = ""
        else:
            # If the character is not the separator, add it to the current substring
            current_substring += char
    
    # Add the last substring to the result
    result.append(current_substring)
    
    # Return the result
    return result

# Test the function
print(split_string("hello world", " "))  # Output: ['hello', 'world']
print(split_string("hello,world", ","))  # Output: ['hello', 'world']