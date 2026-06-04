def canBeTypedWords(text, brokenLetters):
    # Split the text into words
    words = text.split()
    
    # Initialize a counter for the number of words that can be typed
    count = 0
    
    # Iterate over each word in the text
    for word in words:
        # Assume the word can be typed
        can_type = True
        
        # Iterate over each broken letter
        for letter in brokenLetters:
            # If the word contains the broken letter, it cannot be typed
            if letter in word:
                can_type = False
                break
        
        # If the word can be typed, increment the counter
        if can_type:
            count += 1
    
    # Return the number of words that can be typed
    return count