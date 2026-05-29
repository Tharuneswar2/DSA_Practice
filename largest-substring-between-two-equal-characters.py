def largest_substring_between_equal_chars(s):
    # Initialize variables to store the maximum length and the last seen index of each character
    max_length = 0
    last_seen = {}

    # Iterate over the string
    for i, char in enumerate(s):
        # If the character is already in the last_seen dictionary, it means we've found a pair of equal characters
        if char in last_seen:
            # Calculate the length of the substring between the two equal characters
            length = i - last_seen[char] - 1
            # Update the maximum length if the current length is greater
            max_length = max(max_length, length)
        # Update the last seen index of the character
        last_seen[char] = i

    return max_length

def largest_substring_between_equal_chars_alternative(s):
    # Initialize variables to store the maximum length
    max_length = 0

    # Iterate over each unique character in the string
    for char in set(s):
        # Find all occurrences of the character in the string
        indices = [i for i, x in enumerate(s) if x == char]
        # If there are at least two occurrences of the character
        if len(indices) > 1:
            # Calculate the length of the substring between the first and last occurrences of the character
            length = indices[-1] - indices[0] - 1
            # Update the maximum length if the current length is greater
            max_length = max(max_length, length)

    return max_length