# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def canBeTypedWords(text, brokenLetters):
    # Split the input text into words
    words = text.split()
    
    # Initialize a counter to store the number of words that can be typed
    count = 0
    
    # Iterate over each word in the text
    for word in words:
        # Assume the word can be typed initially
        can_type = True
        
        # Iterate over each broken letter
        for letter in brokenLetters:
            # If the word contains a broken letter, it cannot be typed
            if letter in word:
                can_type = False
                break
        
        # If the word can be typed, increment the counter
        if can_type:
            count += 1
    
    # Return the total number of words that can be typed
    return count