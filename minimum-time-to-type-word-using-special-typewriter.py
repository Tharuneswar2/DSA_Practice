def minTimeToType(word: str) -> int:
    # Initialize the total time to type the word
    total_time = 0
    
    # Initialize the previous character
    prev_char = None
    
    # Iterate over each character in the word
    for char in word:
        # If the character is the same as the previous character, 
        # we can type it in 1 second
        if char == prev_char:
            total_time += 1
        else:
            # If the character is different from the previous character, 
            # we need to find the minimum time to type it
            # We can either type it from the beginning or from the previous character
            # The minimum time is the minimum of the two options
            total_time += min(abs(ord(char) - ord('a')), abs(ord(char) - ord(prev_char))) + 1
        
        # Update the previous character
        prev_char = char
    
    # Return the total time to type the word
    return total_time