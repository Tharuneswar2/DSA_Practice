# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def balancedString(s):
    # Initialize a dictionary to store the frequency of each character in the string
    freq = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
    
    # Count the frequency of each character in the string
    for char in s:
        if char in freq:
            freq[char] += 1
    
    # Calculate the ideal frequency of each character in a balanced string
    ideal_freq = len(s) // 4
    
    # Initialize variables to store the minimum length of the substring and the result
    min_len = float('inf')
    result = ""
    
    # Initialize two pointers for the sliding window
    left = 0
    right = 0
    
    # Initialize a dictionary to store the frequency of each character in the current window
    window_freq = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
    
    # Initialize a variable to store the number of characters that are in balance in the current window
    balance_count = 0
    
    # Expand the window to the right
    while right < len(s):
        # Add the character at the right pointer to the window frequency
        if s[right] in freq:
            window_freq[s[right]] += 1
            
            # If the frequency of the character in the window is less than or equal to the ideal frequency, increment the balance count
            if window_freq[s[right]] <= ideal_freq:
                balance_count += 1
        
        # While the window is balanced and the left pointer is less than the right pointer
        while balance_count == 4 and left <= right:
            # Update the minimum length and the result if the current window is smaller
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right + 1]
            
            # Remove the character at the left pointer from the window frequency
            if s[left] in freq:
                if window_freq[s[left]] <= ideal_freq:
                    balance_count -= 1
                window_freq[s[left]] -= 1
            
            # Move the left pointer to the right
            left += 1
        
        # Move the right pointer to the right
        right += 1
    
    # Return the result
    return result