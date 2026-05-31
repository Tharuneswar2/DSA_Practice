def countAsterisks(s):
    # Split the string into substrings separated by '|'
    substrings = s.split('|')
    
    # Initialize a counter for asterisks
    count = 0
    
    # Iterate over the substrings with their indices
    for i, substring in enumerate(substrings):
        # If the index is even, count the asterisks in the substring
        if i % 2 == 0:
            count += substring.count('*')
    
    # Return the total count of asterisks
    return count