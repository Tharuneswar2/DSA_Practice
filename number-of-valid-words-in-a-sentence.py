def countValidWords(sentence: str) -> int:
    # Split the sentence into words
    words = sentence.split()
    
    # Initialize a counter for valid words
    valid_words = 0
    
    # Iterate over each word in the sentence
    for word in words:
        # Initialize a flag to indicate if the word is valid
        is_valid = True
        
        # Check if the word contains any digits
        if any(char.isdigit() for char in word):
            # If the word contains a digit, it's not valid
            is_valid = False
        
        # Check if the word contains any hyphens
        if '-' in word:
            # If the word contains a hyphen, check if it's in a valid position
            if word.count('-') > 1 or word[0] == '-' or word[-1] == '-':
                # If the hyphen is not in a valid position, the word is not valid
                is_valid = False
            else:
                # If the hyphen is in a valid position, split the word into sub-words
                sub_words = word.split('-')
                # Check if the sub-words are valid
                if not all(sub_word.isalpha() for sub_word in sub_words):
                    # If the sub-words are not valid, the word is not valid
                    is_valid = False
        
        # Check if the word contains any punctuation
        if any(not char.isalnum() and char != '-' and char != ' ' for char in word):
            # If the word contains punctuation, it's not valid
            is_valid = False
        
        # Check if the word is a single punctuation mark
        if len(word) == 1 and not word.isalnum():
            # If the word is a single punctuation mark, it's not valid
            is_valid = False
        
        # If the word is valid, increment the counter
        if is_valid:
            valid_words += 1
    
    # Return the count of valid words
    return valid_words