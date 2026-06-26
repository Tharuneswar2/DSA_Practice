def capitalizeTitle(title: str) -> str:
    # Split the title into words
    words = title.split()
    
    # Initialize an empty list to store the capitalized words
    capitalized_words = []
    
    # Iterate over each word in the title
    for word in words:
        # If the word has more than 2 characters, capitalize it
        if len(word) > 2:
            capitalized_words.append(word.capitalize())
        # If the word has 2 or less characters, convert it to lowercase
        else:
            capitalized_words.append(word.lower())
    
    # Join the capitalized words back into a string
    capitalized_title = ' '.join(capitalized_words)
    
    # Return the capitalized title
    return capitalized_title