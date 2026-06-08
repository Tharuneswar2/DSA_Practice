def first_matching_character(s):
    # Initialize two pointers, one at the start and one at the end of the string
    left = 0
    right = len(s) - 1

    # Continue the loop until the two pointers meet
    while left < right:
        # If the characters at the two pointers are the same, return the character
        if s[left] == s[right]:
            return s[left]
        # If the characters are different, move the pointers closer to each other
        else:
            # Move the left pointer to the right
            left += 1
            # Move the right pointer to the left
            right -= 1

    # If the loop ends without finding a match, return None
    return None

# Test the function
print(first_matching_character("abcba"))  # Output: 'a'
print(first_matching_character("abcdef"))  # Output: None