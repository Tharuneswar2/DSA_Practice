def similarPairs(words):
    # Create a hashmap to store the frequency of each word's bitmask
    bitmask_freq = {}
    
    # Initialize the count of similar pairs
    similar_pairs = 0
    
    # Iterate over each word in the list
    for word in words:
        # Initialize the bitmask for the current word
        bitmask = 0
        
        # Iterate over each character in the word
        for char in word:
            # Update the bitmask by setting the bit corresponding to the character
            bitmask |= 1 << (ord(char) - ord('a'))
        
        # If the bitmask is already in the hashmap, increment the count of similar pairs
        if bitmask in bitmask_freq:
            similar_pairs += bitmask_freq[bitmask]
            # Increment the frequency of the bitmask
            bitmask_freq[bitmask] += 1
        else:
            # Otherwise, add the bitmask to the hashmap with a frequency of 1
            bitmask_freq[bitmask] = 1
    
    # Return the count of similar pairs
    return similar_pairs

def numSpecial(words):
    # Create a hashmap to store the frequency of each word
    word_freq = {}
    
    # Initialize the count of special pairs
    special_pairs = 0
    
    # Iterate over each word in the list
    for word in words:
        # If the word is already in the hashmap, increment the count of special pairs
        if word in word_freq:
            special_pairs += word_freq[word]
            # Increment the frequency of the word
            word_freq[word] += 1
        else:
            # Otherwise, add the word to the hashmap with a frequency of 1
            word_freq[word] = 1
    
    # Return the count of special pairs
    return special_pairs