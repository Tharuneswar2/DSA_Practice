def is_prefix_of_array(s, words):
    # Initialize an empty string to store the concatenated words
    concatenated_str = ""
    
    # Iterate over each word in the list of words
    for word in words:
        # Concatenate the current word to the concatenated string
        concatenated_str += word
        
        # Check if the concatenated string is equal to the given string
        if concatenated_str == s:
            # If it is, return True
            return True
        
        # If the concatenated string is longer than the given string, 
        # it's impossible for the given string to be a prefix of the array
        if len(concatenated_str) > len(s):
            # So, break out of the loop
            break
    
    # If the loop completes without finding a match, return False
    return False