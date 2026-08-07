# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def freqAlphabets(s):
    # Initialize an empty string to store the decrypted result
    result = ''
    
    # Initialize a pointer to the end of the string
    i = len(s) - 1
    
    # Iterate through the string from the end to the start
    while i >= 0:
        # If the current character is '#', it means we have a 2-digit number
        if s[i] == '#':
            # Extract the 2-digit number and convert it to a character
            result = chr(96 + int(s[i-2:i])) + result
            # Move the pointer 3 steps back
            i -= 3
        else:
            # If the current character is not '#', it's a single digit number
            # Convert it to a character and add it to the result
            result = chr(96 + int(s[i])) + result
            # Move the pointer 1 step back
            i -= 1
    
    # Return the decrypted result
    return result