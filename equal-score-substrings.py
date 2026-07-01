def equal_score_substrings(s):
    # Initialize a dictionary to store the frequency of each character
    char_freq = {}
    
    # Initialize variables to store the total score and the result
    total_score = 0
    result = []
    
    # Calculate the total score by counting the frequency of each character
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
        total_score += char_freq[char]
    
    # Initialize variables to store the current score and the start index
    curr_score = 0
    start = 0
    
    # Iterate over the string to find equal score substrings
    for end, char in enumerate(s):
        # Increment the current score by the frequency of the current character
        curr_score += char_freq[char]
        
        # While the current score is greater than half of the total score, 
        # decrement the current score by the frequency of the character at the start index and increment the start index
        while curr_score > total_score // 2:
            curr_score -= char_freq[s[start]]
            start += 1
        
        # If the current score is equal to half of the total score, add the substring to the result
        if curr_score == total_score // 2:
            result.append(s[start:end+1])
    
    return result