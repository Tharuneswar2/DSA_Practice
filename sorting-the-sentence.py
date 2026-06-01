def sort_sentence(s):
    # Split the sentence into words
    words = s.split()
    
    # Initialize an empty list to store the sorted words
    sorted_words = [''] * len(words)
    
    # Iterate over each word in the sentence
    for word in words:
        # Find the index of the word (last character of the word)
        index = int(word[-1]) - 1
        
        # Remove the index from the word
        word = word[:-1]
        
        # Place the word at its correct position in the sorted_words list
        sorted_words[index] = word
    
    # Join the sorted words into a sentence
    sorted_sentence = ' '.join(sorted_words)
    
    return sorted_sentence

# Test the function
print(sort_sentence("is2 sentence4 This1 a3"))