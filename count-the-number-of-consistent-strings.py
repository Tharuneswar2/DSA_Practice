def countConsistentStrings(allowed, words):
    # Convert the allowed string into a set for efficient lookups
    allowed_set = set(allowed)
    
    # Initialize a counter for consistent strings
    consistent_count = 0
    
    # Iterate over each word in the list of words
    for word in words:
        # Assume the word is consistent initially
        is_consistent = True
        
        # Iterate over each character in the word
        for char in word:
            # If the character is not in the allowed set, the word is not consistent
            if char not in allowed_set:
                is_consistent = False
                break
        
        # If the word is consistent, increment the counter
        if is_consistent:
            consistent_count += 1
    
    # Return the count of consistent strings
    return consistent_count