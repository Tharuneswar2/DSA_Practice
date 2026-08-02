# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def first_palindromic_string(arr):
    # Iterate over each string in the input array
    for string in arr:
        # Initialize two pointers, one at the start and one at the end of the string
        left, right = 0, len(string) - 1
        
        # Continue the loop until the two pointers meet
        while left < right:
            # If the characters at the two pointers are not equal, the string is not a palindrome
            if string[left] != string[right]:
                break
            # Move the pointers closer to the center of the string
            left, right = left + 1, right - 1
        
        # If the loop completes without finding a mismatch, the string is a palindrome
        else:
            # Return the first palindromic string found
            return string
    
    # If no palindromic string is found, return None
    return None