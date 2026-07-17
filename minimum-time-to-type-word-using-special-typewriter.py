# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def minTimeToType(word: str) -> int:
    # Initialize the total time to type the word
    total_time = 0
    
    # Initialize the previous character to None
    prev_char = None
    
    # Iterate over each character in the word
    for char in word:
        # If the previous character is not None and it's different from the current character
        if prev_char is not None and prev_char != char:
            # Calculate the minimum time to move to the current character
            # This is done by taking the minimum between the absolute difference between the ASCII values of the two characters
            # and 26 minus this difference (because we can move in both clockwise and counter-clockwise directions)
            min_time = min(abs(ord(char) - ord(prev_char)), 26 - abs(ord(char) - ord(prev_char)))
            # Add the minimum time to the total time
            total_time += min_time
        
        # Add 1 to the total time because we need to type the current character
        total_time += 1
        
        # Update the previous character
        prev_char = char
    
    # Return the total time
    return total_time