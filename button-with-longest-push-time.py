def isPrefixString(s, words):
    # Initialize an empty string to store the prefix
    prefix = ""
    
    # Iterate over each word in the list of words
    for word in words:
        # Append the current word to the prefix
        prefix += word
        
        # Check if the prefix is equal to the given string
        if prefix == s:
            # If it is, return True
            return True
        
        # If the prefix is longer than the string, break the loop
        if len(prefix) > len(s):
            break
    
    # If the loop completes without finding a match, return False
    return False

def isPrefixStringAlternative(s, words):
    # Initialize a variable to store the prefix length
    prefix_length = 0
    
    # Iterate over each word in the list of words
    for word in words:
        # Add the length of the current word to the prefix length
        prefix_length += len(word)
        
        # Check if the prefix length is equal to the length of the string
        if prefix_length == len(s):
            # If it is, return True
            return True
        
        # If the prefix length is longer than the string, break the loop
        if prefix_length > len(s):
            break
    
    # If the loop completes without finding a match, return False
    return False

def isPrefixStringAlternativeTwo(s, words):
    # Join all the words in the list into a single string
    prefix = "".join(words)
    
    # Check if the string starts with the prefix
    return s == prefix[:len(s)]

def isPrefixStringAlternativeThree(s, words):
    # Initialize an empty string to store the prefix
    prefix = ""
    
    # Iterate over each word in the list of words
    for word in words:
        # Append the current word to the prefix
        prefix += word
        
        # Check if the prefix is equal to the given string
        if prefix == s:
            # If it is, return True
            return True
        
        # If the prefix is longer than the string, break the loop
        if len(prefix) > len(s):
            break
    
    # If the loop completes without finding a match, return False
    return False