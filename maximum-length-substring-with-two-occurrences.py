# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def lengthOfLongestSubstringTwoDistinct(s):
    # Initialize variables to store the maximum length and the start of the window
    max_length = 0
    window_start = 0
    
    # Initialize a dictionary to store the frequency of characters in the current window
    char_frequency = {}
    
    # Iterate over the string
    for window_end in range(len(s)):
        # Add the current character to the frequency dictionary
        right_char = s[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1
        
        # Shrink the window if there are more than two distinct characters
        while len(char_frequency) > 2:
            left_char = s[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1
        
        # Update the maximum length
        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length