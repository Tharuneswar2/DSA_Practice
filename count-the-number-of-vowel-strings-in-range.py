# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def vowelStrings(words, left, right):
    # Define the vowels
    vowels = set('aeiou')
    
    # Initialize count of vowel strings
    count = 0
    
    # Iterate over the range of words from left to right (inclusive)
    for i in range(left, right + 1):
        # Check if the first and last characters of the word are vowels
        if words[i][0] in vowels and words[i][-1] in vowels:
            # If they are, increment the count
            count += 1
    
    # Return the count of vowel strings
    return count