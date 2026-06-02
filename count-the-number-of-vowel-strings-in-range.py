def vowelStrings(words, left, right):
    # Define the vowels
    vowels = set('aeiou')
    
    # Initialize count
    count = 0
    
    # Iterate over the range of words
    for i in range(left, right + 1):
        # Check if the first and last characters of the word are vowels
        if words[i][0] in vowels and words[i][-1] in vowels:
            # If they are, increment the count
            count += 1
    
    # Return the count
    return count