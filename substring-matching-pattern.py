def compute_prefix_function(pattern):
    # Initialize the prefix array with zeros
    prefix = [0] * len(pattern)
    j = 0  # Index for the prefix

    # Iterate over the pattern to fill the prefix array
    for i in range(1, len(pattern)):
        # If the current character does not match the prefix character, reset j
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]
        # If the characters match, increment j
        if pattern[i] == pattern[j]:
            j += 1
        # Update the prefix array
        prefix[i] = j

    return prefix


def kmp_search(text, pattern):
    # Compute the prefix function for the pattern
    prefix = compute_prefix_function(pattern)
    j = 0  # Index for the pattern

    # Iterate over the text to find the pattern
    for i in range(len(text)):
        # If the current character does not match the pattern character, reset j
        while j > 0 and text[i] != pattern[j]:
            j = prefix[j - 1]
        # If the characters match, increment j
        if text[i] == pattern[j]:
            j += 1
        # If the entire pattern is found, return the starting index
        if j == len(pattern):
            return i - len(pattern) + 1

    # If the pattern is not found, return -1
    return -1


# Example usage
text = "abxabcabcaby"
pattern = "abcaby"
index = kmp_search(text, pattern)
if index != -1:
    print("Pattern found at index", index)
else:
    print("Pattern not found")