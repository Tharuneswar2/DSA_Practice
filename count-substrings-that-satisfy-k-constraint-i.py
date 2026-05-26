def count_substrings(s, k):
    # Initialize count of substrings
    count = 0
    
    # Iterate over each character in the string
    for i in range(len(s)):
        # Initialize a dictionary to store the frequency of characters in the current substring
        char_freq = {}
        
        # Iterate over each substring starting from the current character
        for j in range(i, len(s)):
            # Increment the frequency of the current character
            char_freq[s[j]] = char_freq.get(s[j], 0) + 1
            
            # If the number of unique characters in the substring is equal to k
            if len(char_freq) == k:
                # Increment the count of substrings
                count += 1
                
    # Return the count of substrings
    return count