# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def modifyString(s):
    # Convert the string into a list of characters for easier manipulation
    s = list(s)
    
    # Iterate over each character in the string
    for i in range(len(s)):
        # If the character is a question mark
        if s[i] == '?':
            # Initialize a set to store the characters that cannot be used
            cannot_use = set()
            
            # If the previous character exists and is not a question mark, add it to the set
            if i > 0 and s[i-1] != '?':
                cannot_use.add(s[i-1])
            
            # If the next character exists and is not a question mark, add it to the set
            if i < len(s) - 1 and s[i+1] != '?':
                cannot_use.add(s[i+1])
            
            # Initialize a variable to store the character that can be used
            can_use = None
            
            # Iterate over all lowercase English letters
            for char in 'abcdefghijklmnopqrstuvwxyz':
                # If the character is not in the set of characters that cannot be used
                if char not in cannot_use:
                    # Store the character and break the loop
                    can_use = char
                    break
            
            # Replace the question mark with the character that can be used
            s[i] = can_use
    
    # Join the list of characters back into a string and return it
    return ''.join(s)