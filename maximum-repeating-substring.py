# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def maxRepeating(sequence, word):
    # Initialize a counter to keep track of the maximum repeating substring
    count = 0
    
    # Initialize a temporary string to build the repeating substring
    temp = word
    
    # Continue building the repeating substring as long as it's a substring of the sequence
    while temp in sequence:
        # If the temporary string is a substring of the sequence, increment the counter
        count += 1
        
        # Build the repeating substring by appending the word to the temporary string
        temp += word
    
    # Return the maximum count of the repeating substring
    return count