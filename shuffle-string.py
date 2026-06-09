def restoreString(s, indices):
    # Create a list of tuples where each tuple contains a character from the string and its corresponding index
    indexed_chars = [(char, index) for char, index in zip(s, indices)]
    
    # Sort the list of tuples based on the indices
    indexed_chars.sort(key=lambda x: x[1])
    
    # Join the characters in the sorted order to form the shuffled string
    shuffled_string = ''.join([char for char, index in indexed_chars])
    
    return shuffled_string