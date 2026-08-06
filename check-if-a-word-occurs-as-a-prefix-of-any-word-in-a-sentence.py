# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def check_prefix(sentence, word):
    # Split the sentence into words to check each word individually
    words = sentence.split()
    
    # Iterate over each word in the sentence
    for w in words:
        # Check if the word starts with the given prefix
        if w.startswith(word):
            # If a match is found, return True
            return True
    
    # If no match is found after checking all words, return False
    return False

def check_prefix_efficient(sentence, word):
    # Split the sentence into words to check each word individually
    words = sentence.split()
    
    # Use a generator expression with the any function to check if any word starts with the prefix
    # This approach is more efficient as it stops checking as soon as it finds a match
    return any(w.startswith(word) for w in words)