# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def sortSentence(s):
    # Split the input string into words
    words = s.split()
    
    # Initialize an empty list to store the sorted words
    sorted_words = [''] * len(words)
    
    # Iterate over each word in the input string
    for word in words:
        # Find the index of the word (last character of the word)
        index = int(word[-1]) - 1
        
        # Remove the index from the word and store it in the sorted_words list
        sorted_words[index] = word[:-1]
    
    # Join the sorted words into a sentence and return
    return ' '.join(sorted_words)