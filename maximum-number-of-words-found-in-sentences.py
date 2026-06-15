def mostWordsFound(sentences):
    # Initialize max_words to store the maximum number of words found
    max_words = 0
    
    # Iterate over each sentence in the list of sentences
    for sentence in sentences:
        # Split the sentence into words and count the number of words
        num_words = len(sentence.split())
        
        # Update max_words if the current sentence has more words
        max_words = max(max_words, num_words)
    
    # Return the maximum number of words found
    return max_words

# Alternatively, using a one-liner with max and a generator expression
def mostWordsFound(sentences):
    # Use max to find the maximum number of words in any sentence
    # The generator expression splits each sentence into words and counts them
    return max(len(sentence.split()) for sentence in sentences)