# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def special_substring(s, k):
    # Initialize a hashmap to store the frequency of each character in the string
    char_freq = {}
    
    # Initialize variables to store the start of the window, the number of unique characters in the window, and the result
    window_start = 0
    unique_chars = 0
    result = ""
    
    # Iterate over the string
    for window_end in range(len(s)):
        # Add the current character to the hashmap and increment its frequency
        right_char = s[window_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
            unique_chars += 1
        char_freq[right_char] += 1
        
        # If the window size is greater than k, shrink the window from the left
        if window_end >= k - 1:
            # If the number of unique characters in the window is equal to the window size, update the result
            if unique_chars == k:
                result = s[window_start:window_end + 1]
            
            # Remove the leftmost character from the hashmap and decrement its frequency
            left_char = s[window_start]
            char_freq[left_char] -= 1
            if char_freq[left_char] == 0:
                del char_freq[left_char]
                unique_chars -= 1
            
            # Move the window to the right
            window_start += 1
    
    # Return the result
    return result