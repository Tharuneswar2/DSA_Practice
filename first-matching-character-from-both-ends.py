# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def firstMatchingCharacter(s):
    # Initialize two pointers, one at the start and one at the end of the string
    left = 0
    right = len(s) - 1
    
    # Continue the loop until the two pointers meet
    while left < right:
        # If the characters at the two pointers are the same, return the character
        if s[left] == s[right]:
            return s[left]
        # If the character at the left pointer is not equal to the character at the right pointer
        # Move the pointer of the character that appears first in the alphabet
        elif s[left] < s[right]:
            # Move the right pointer to the left
            right -= 1
        else:
            # Move the left pointer to the right
            left += 1
            
    # If no matching character is found, return None
    return None