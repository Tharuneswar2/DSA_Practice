# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def capitalizeTitle(title: str) -> str:
    # Split the title into words
    words = title.split()
    
    # Initialize an empty list to store the capitalized words
    capitalized_words = []
    
    # Iterate over each word in the title
    for word in words:
        # If the word has more than 2 characters, capitalize the first letter and make the rest lowercase
        if len(word) > 2:
            capitalized_word = word.capitalize()
        # If the word has 2 or less characters, make it lowercase
        else:
            capitalized_word = word.lower()
        
        # Add the capitalized word to the list
        capitalized_words.append(capitalized_word)
    
    # Join the capitalized words back into a string with spaces in between
    capitalized_title = ' '.join(capitalized_words)
    
    # Return the capitalized title
    return capitalized_title