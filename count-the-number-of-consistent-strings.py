# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def countConsistentStrings(allowed, words):
    # Convert the allowed string into a set for efficient lookups
    allowed_set = set(allowed)
    
    # Initialize a counter to store the count of consistent strings
    count = 0
    
    # Iterate over each word in the list of words
    for word in words:
        # Assume the word is consistent initially
        is_consistent = True
        
        # Iterate over each character in the word
        for char in word:
            # If the character is not in the allowed set, the word is not consistent
            if char not in allowed_set:
                is_consistent = False
                # Break the loop as we don't need to check the rest of the characters
                break
        
        # If the word is consistent, increment the count
        if is_consistent:
            count += 1
    
    # Return the count of consistent strings
    return count