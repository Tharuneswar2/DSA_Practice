def are_all_chars_equal(s):
    # Create a dictionary to store the frequency of each character
    char_freq = {}
    
    # Iterate over the string to count the frequency of each character
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    # Get the frequency of the first character
    expected_freq = char_freq[s[0]]
    
    # Check if all characters have the same frequency
    for freq in char_freq.values():
        if freq != expected_freq:
            return False
    
    return True

# Test the function
print(are_all_chars_equal("aabbcc"))  # True
print(are_all_chars_equal("aabbbbcc"))  # False