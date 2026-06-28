def check_prefix(sentence, word):
    # Split the sentence into words
    words = sentence.split()
    
    # Iterate over each word in the sentence
    for w in words:
        # Check if the word starts with the given prefix
        if w.startswith(word):
            # If it does, return True
            return True
    
    # If no word starts with the prefix, return False
    return False

# Test the function
print(check_prefix("Hello world this is a test", "wor"))  # Returns: True
print(check_prefix("Hello world this is a test", "abc"))  # Returns: False