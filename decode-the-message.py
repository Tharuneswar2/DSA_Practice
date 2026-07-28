# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def decodeMessage(key, message):
    # Create a dictionary to store the mapping of keys to characters
    key_map = {}
    
    # Initialize the character counter to 'a'
    char = 'a'
    
    # Iterate over each character in the key
    for k in key:
        # If the character is not already in the dictionary and it's not a space
        if k not in key_map and k != ' ':
            # Map the character to the current character in the alphabet
            key_map[k] = char
            # Move to the next character in the alphabet
            char = chr(ord(char) + 1)
    
    # Initialize an empty string to store the decoded message
    decoded_message = ''
    
    # Iterate over each character in the message
    for m in message:
        # If the character is a space, add a space to the decoded message
        if m == ' ':
            decoded_message += ' '
        # Otherwise, add the mapped character to the decoded message
        else:
            decoded_message += key_map[m]
    
    # Return the decoded message
    return decoded_message