# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def compute_prefix_function(pattern):
    # Initialize the prefix array with zeros
    prefix = [0] * len(pattern)
    # Initialize the prefix and suffix pointers
    j = 0
    # Iterate over the pattern to fill the prefix array
    for i in range(1, len(pattern)):
        # If the current character in the pattern does not match the character at the prefix pointer
        while j > 0 and pattern[i] != pattern[j]:
            # Move the prefix pointer to the previous prefix
            j = prefix[j - 1]
        # If the current character in the pattern matches the character at the prefix pointer
        if pattern[i] == pattern[j]:
            # Move the prefix pointer forward
            j += 1
        # Update the prefix array
        prefix[i] = j
    return prefix

def kmp_search(text, pattern):
    # Compute the prefix function for the pattern
    prefix = compute_prefix_function(pattern)
    # Initialize the text and pattern pointers
    i = j = 0
    # Iterate over the text to find the pattern
    while i < len(text):
        # If the current character in the text matches the character at the pattern pointer
        if text[i] == pattern[j]:
            # Move both pointers forward
            i += 1
            j += 1
        # If the entire pattern has been found
        if j == len(pattern):
            # Return the starting index of the pattern in the text
            return i - j
        # If the current character in the text does not match the character at the pattern pointer
        elif i < len(text) and text[i] != pattern[j]:
            # If the pattern pointer is not at the beginning of the pattern
            if j != 0:
                # Move the pattern pointer to the previous prefix
                j = prefix[j - 1]
            else:
                # Move the text pointer forward
                i += 1
    # If the pattern is not found in the text
    return -1

def substring_matching_pattern(text, pattern):
    # Use the KMP algorithm to search for the pattern in the text
    return kmp_search(text, pattern)

text = "abcabcabc"
pattern = "abc"
print(substring_matching_pattern(text, pattern))