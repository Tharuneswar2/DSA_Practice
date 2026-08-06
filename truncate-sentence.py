# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def truncateSentence(s, k):
    # Split the input string into a list of words
    words = s.split()
    
    # Use list slicing to get the first k words
    truncated_words = words[:k]
    
    # Join the truncated words back into a string separated by spaces
    truncated_sentence = ' '.join(truncated_words)
    
    # Return the truncated sentence
    return truncated_sentence