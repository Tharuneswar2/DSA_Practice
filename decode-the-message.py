def decode_message(key, message):
    # Create a dictionary to store the mapping of numbers to letters
    mapping = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Populate the mapping dictionary
    for i in range(26):
        mapping[str(i+1)] = alphabet[i]
    
    # Initialize an empty string to store the decoded message
    decoded_message = ''
    
    # Split the message into words
    words = message.split()
    
    # Iterate over each word in the message
    for word in words:
        # Initialize an empty string to store the decoded word
        decoded_word = ''
        
        # Iterate over each character in the word
        for char in word:
            # If the character is a digit, add the corresponding letter to the decoded word
            if char.isdigit():
                decoded_word += mapping[char]
            # If the character is a space, add a space to the decoded word
            elif char == ' ':
                decoded_word += ' '
        
        # Add the decoded word to the decoded message
        decoded_message += decoded_word + ' '
    
    # Return the decoded message
    return decoded_message.strip()

# Example usage:
key = '123'
message = '1 23 2 1 20 8 5 19 7 15 14 7 5 20 8 5 19'
print(decode_message(key, message))