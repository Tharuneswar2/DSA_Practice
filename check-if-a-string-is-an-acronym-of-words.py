def is_acronym(s, words):
    # Convert the string to uppercase for case-insensitive comparison
    s = s.upper()
    
    # Initialize an empty string to store the acronym
    acronym = ''
    
    # Iterate over each word in the list of words
    for word in words:
        # Extract the first character of the word and convert it to uppercase
        first_char = word[0].upper()
        
        # Add the first character to the acronym
        acronym += first_char
    
    # Check if the acronym matches the given string
    return acronym == s

# Example usage:
print(is_acronym('ABC', ['Alpha', 'Beta', 'Computer']))  # Returns: True
print(is_acronym('ABC', ['Alpha', 'Beta', 'Code']))  # Returns: False