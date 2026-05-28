def numOfStrings(words, parts):
    # Initialize count to store the number of strings that appear as substrings
    count = 0
    
    # Iterate over each word in the words list
    for word in words:
        # Iterate over each part in the parts list
        for part in parts:
            # Check if the part is a substring of the word
            if part in word:
                # If it is, increment the count
                count += 1
                # Break the loop as we don't need to check other parts for this word
                break
    
    # Return the count
    return count