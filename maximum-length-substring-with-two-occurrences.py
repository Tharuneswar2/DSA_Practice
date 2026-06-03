def length_of_longest_substring_two_distinct(s):
    # Initialize variables to store the maximum length and the last seen index of each character
    max_length = 0
    last_seen = {}
    window_start = 0
    
    # Iterate over the string
    for window_end in range(len(s)):
        # Add the current character to the last seen dictionary
        right_char = s[window_end]
        if right_char not in last_seen:
            last_seen[right_char] = 0
        last_seen[right_char] += 1
        
        # While there are more than two distinct characters in the window, shrink the window
        while len(last_seen) > 2:
            left_char = s[window_start]
            last_seen[left_char] -= 1
            if last_seen[left_char] == 0:
                del last_seen[left_char]
            window_start += 1
        
        # Update the maximum length
        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length