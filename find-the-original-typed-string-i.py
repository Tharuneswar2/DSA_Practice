def originalTypedString(typed, target):
    # Initialize two pointers for the typed and target strings
    i = j = 0
    
    # Initialize a flag to track if we are currently in a sequence of repeated characters
    in_sequence = False
    
    # Initialize the result string
    result = ''
    
    # Iterate over the typed string
    while i < len(typed):
        # If the current character in the typed string matches the current character in the target string
        if j < len(target) and typed[i] == target[j]:
            # If we are not in a sequence of repeated characters, add the character to the result string
            if not in_sequence:
                result += typed[i]
            # Move to the next character in the target string
            j += 1
            # Move to the next character in the typed string
            i += 1
            # Reset the flag
            in_sequence = False
        # If the current character in the typed string is a repeat of the previous character
        elif i > 0 and typed[i] == typed[i-1]:
            # Set the flag to indicate that we are in a sequence of repeated characters
            in_sequence = True
            # Move to the next character in the typed string
            i += 1
        # If the current character in the typed string does not match the current character in the target string
        else:
            # If we are in a sequence of repeated characters, remove the last character from the result string
            if in_sequence:
                result = result[:-1]
            # Move to the next character in the typed string
            i += 1
            # Reset the flag
            in_sequence = False
    
    # Return the result string
    return result