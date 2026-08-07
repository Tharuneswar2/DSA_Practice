# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def compute_prefix_function(pattern):
    # Initialize the prefix array with zeros
    prefix = [0] * len(pattern)
    # Initialize the length of the longest proper prefix which is also a suffix
    length = 0
    # Iterate over the pattern to fill the prefix array
    for i in range(1, len(pattern)):
        # If the current character does not match the character at the current length
        while length > 0 and pattern[i] != pattern[length]:
            # Update the length to the value at the previous index in the prefix array
            length = prefix[length - 1]
        # If the current character matches the character at the current length
        if pattern[i] == pattern[length]:
            # Increment the length
            length += 1
        # Update the prefix array with the current length
        prefix[i] = length
    return prefix

def substring_matching_pattern(text, pattern):
    # Compute the prefix array for the pattern
    prefix = compute_prefix_function(pattern)
    # Initialize the length of the longest proper prefix which is also a suffix
    length = 0
    # Iterate over the text to find the pattern
    for i in range(len(text)):
        # If the current character does not match the character at the current length
        while length > 0 and text[i] != pattern[length]:
            # Update the length to the value at the previous index in the prefix array
            length = prefix[length - 1]
        # If the current character matches the character at the current length
        if text[i] == pattern[length]:
            # Increment the length
            length += 1
        # If the length is equal to the length of the pattern
        if length == len(pattern):
            # Return the starting index of the pattern in the text
            return i - len(pattern) + 1
    # If the pattern is not found in the text
    return -1