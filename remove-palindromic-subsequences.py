def remove_palindromic_subsequences(s: str) -> int:
    # If the string is empty, return 0
    if not s:
        return 0
    
    # If the string is a palindrome, return 1
    if s == s[::-1]:
        return 1
    
    # Initialize two pointers, one at the start and one at the end of the string
    left, right = 0, len(s) - 1
    
    # Initialize a flag to check if the string is a palindrome
    is_palindrome = True
    
    # Compare characters from the start and end of the string
    while left < right:
        # If the characters are not equal, the string is not a palindrome
        if s[left] != s[right]:
            is_palindrome = False
            break
        # Move the pointers towards the center of the string
        left += 1
        right -= 1
    
    # If the string is a palindrome, return 1
    if is_palindrome:
        return 1
    
    # If the string is not a palindrome, return 2
    return 2