# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def similarPairs(words):
    # Create a hashmap to store the frequency of each word's character set
    freq_map = {}
    
    # Initialize the count of similar pairs
    similar_pairs = 0
    
    # Iterate over each word in the list
    for word in words:
        # Create a set of characters in the word and convert it to a tuple (since sets are not hashable)
        char_set = tuple(sorted(set(word)))
        
        # If the character set is already in the hashmap, increment the count of similar pairs
        if char_set in freq_map:
            # The number of similar pairs for the current word is the frequency of its character set
            similar_pairs += freq_map[char_set]
            # Increment the frequency of the character set
            freq_map[char_set] += 1
        else:
            # If the character set is not in the hashmap, add it with a frequency of 1
            freq_map[char_set] = 1
    
    # Return the total count of similar pairs
    return similar_pairs