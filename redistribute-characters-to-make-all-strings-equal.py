def makeEqual(words):
    # Create a dictionary to store the frequency of each character
    char_freq = {}
    
    # Iterate over each word in the list of words
    for word in words:
        # Iterate over each character in the word
        for char in word:
            # If the character is already in the dictionary, increment its frequency
            if char in char_freq:
                char_freq[char] += 1
            # If the character is not in the dictionary, add it with a frequency of 1
            else:
                char_freq[char] = 1
                
    # Calculate the number of strings
    num_strings = len(words)
    
    # Iterate over each character and its frequency in the dictionary
    for char, freq in char_freq.items():
        # If the frequency of the character is not divisible by the number of strings, return False
        if freq % num_strings != 0:
            return False
            
    # If we have not returned False by now, it means we can redistribute the characters to make all strings equal
    return True