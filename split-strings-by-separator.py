def split_string(s, sep):
    # If the separator is empty, split the string into individual characters
    if not sep:
        return list(s)
    
    # Initialize an empty list to store the split strings
    result = []
    
    # Initialize an empty string to build the current substring
    current = ""
    
    # Iterate over each character in the input string
    for char in s:
        # If the character is the separator, add the current substring to the result and reset it
        if char == sep:
            result.append(current)
            current = ""
        # Otherwise, add the character to the current substring
        else:
            current += char
    
    # Add the last substring to the result if it's not empty
    if current:
        result.append(current)
    
    return result

# Test the function
print(split_string("hello world", " "))  # Output: ["hello", "world"]
print(split_string("abcdefg", ""))  # Output: ["a", "b", "c", "d", "e", "f", "g"]