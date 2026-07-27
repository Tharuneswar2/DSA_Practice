# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def equal_score_substrings(s):
    # Initialize a dictionary to store the frequency of each character in the string
    char_freq = {}
    
    # Initialize variables to store the total score and the number of equal score substrings
    total_score = 0
    equal_score_substrings = 0
    
    # Calculate the total score by iterating over the string and updating the frequency dictionary
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
        total_score += char_freq[char]
    
    # Initialize variables to store the current score and the number of characters in the current substring
    curr_score = 0
    curr_chars = 0
    
    # Initialize two pointers, one at the start and one at the end of the string
    left = 0
    right = 0
    
    # Iterate over the string using the two pointers
    while right < len(s):
        # If the current score is less than half of the total score, move the right pointer to the right
        if curr_score < total_score / 2:
            curr_score += char_freq[s[right]]
            curr_chars += 1
            right += 1
        # If the current score is greater than half of the total score, move the left pointer to the right
        elif curr_score > total_score / 2:
            curr_score -= char_freq[s[left]]
            curr_chars -= 1
            left += 1
        # If the current score is equal to half of the total score, increment the count of equal score substrings
        else:
            equal_score_substrings += 1
            curr_score -= char_freq[s[left]]
            curr_chars -= 1
            left += 1
    
    # Return the count of equal score substrings
    return equal_score_substrings