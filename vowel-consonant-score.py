def score_words(words):
    # Initialize the score
    score = 0
    
    # Iterate over each word in the list
    for word in words:
        # Initialize the vowel count for the current word
        vowel_count = 0
        
        # Iterate over each character in the word
        for char in word:
            # Check if the character is a vowel
            if char.lower() in 'aeiou':
                # If it's a vowel, increment the vowel count
                vowel_count += 1
        
        # If the vowel count is greater than the number of consonants, 
        # increment the score by the vowel count
        if vowel_count > (len(word) - vowel_count):
            score += vowel_count
        # Otherwise, increment the score by the number of consonants
        else:
            score += (len(word) - vowel_count)
    
    # Return the total score
    return score