# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def reorderSpaces(text):
    # Split the input string into words and count the total number of spaces
    words = text.split()
    total_spaces = text.count(' ')
    
    # If there are multiple words, distribute the spaces evenly between them
    if len(words) > 1:
        # Calculate the number of spaces to be added between each word
        space_between_words = total_spaces // (len(words) - 1)
        # Calculate the remaining spaces to be added at the end
        remaining_spaces = total_spaces % (len(words) - 1)
        
        # Initialize the result string with the first word
        result = words[0]
        # Add the calculated number of spaces and the next word to the result string
        for word in words[1:]:
            result += ' ' * space_between_words + word
        # Add the remaining spaces at the end of the result string
        result += ' ' * remaining_spaces
    else:
        # If there's only one word, add all the spaces at the end
        result = words[0] + ' ' * total_spaces
    
    return result