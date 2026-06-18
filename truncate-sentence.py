def truncate_sentence(sentence, k):
    # Split the sentence into words
    words = sentence.split()
    
    # If the number of words is less than or equal to k, return the original sentence
    if len(words) <= k:
        return sentence
    
    # Otherwise, truncate the sentence to k words and join them back into a string
    else:
        return ' '.join(words[:k]) + '...'

# Test the function
print(truncate_sentence("Hello world this is a test", 3))