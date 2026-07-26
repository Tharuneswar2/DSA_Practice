# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def count_special_characters(s):
    # Initialize a counter variable to store the count of special characters
    count = 0
    
    # Define a string of special characters
    special_chars = "!@#$%^&*()-+?_=,<>/"
    
    # Iterate over each character in the input string
    for char in s:
        # Check if the character is in the string of special characters
        if char in special_chars:
            # If the character is special, increment the counter
            count += 1
    
    # Return the count of special characters
    return count