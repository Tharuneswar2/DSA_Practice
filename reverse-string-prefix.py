def reverse_prefix(s, ch):
    # Find the index of the character in the string
    idx = s.find(ch)
    
    # If the character is not found, return the original string
    if idx == -1:
        return s
    
    # Reverse the substring from the start to the index of the character
    prefix = s[:idx+1][::-1]
    
    # Concatenate the reversed prefix with the rest of the string
    return prefix + s[idx+1:]

# Test the function
print(reverse_prefix("abcdefd", "d"))  # Output: "dcbaefd"