# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def reversePrefix(s, ch):
    # Convert the string into a list of characters for easier manipulation
    s = list(s)
    
    # Initialize two pointers, one at the start and one at the end of the string
    left, right = 0, 0
    
    # Find the index of the character that we need to reverse up to
    while right < len(s) and s[right] != ch:
        right += 1
    
    # If the character is not found, return the original string
    if right == len(s):
        return ''.join(s)
    
    # Reverse the substring from the start to the character
    while left < right:
        # Swap the characters at the left and right pointers
        s[left], s[right] = s[right], s[left]
        # Move the pointers towards each other
        left += 1
        right -= 1
    
    # Convert the list of characters back into a string and return it
    return ''.join(s)