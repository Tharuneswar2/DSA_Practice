# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def numOfStrings(words, parts):
    # Initialize a counter to store the number of strings that appear as substrings in word
    count = 0
    
    # Iterate over each word in the words list
    for word in words:
        # Iterate over each part in the parts list
        for part in parts:
            # Check if the part is a substring of the word
            if part in word:
                # If the part is a substring, increment the count
                count += 1
                # Break the loop as we don't need to check the rest of the parts
                break
                
    # Return the count of strings that appear as substrings in word
    return count