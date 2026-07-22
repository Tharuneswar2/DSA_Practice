# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def sortSentence(s):
    # Split the input string into a list of words
    words = s.split()
    
    # Initialize an empty list to store the sorted words
    sorted_words = [''] * len(words)
    
    # Iterate over each word in the list of words
    for word in words:
        # Find the index of the word by getting the last character (which is the index) and converting it to an integer
        index = int(word[-1]) - 1
        
        # Remove the last character (the index) from the word
        word = word[:-1]
        
        # Place the word at its correct index in the sorted_words list
        sorted_words[index] = word
    
    # Join the sorted words into a single string separated by spaces
    return ' '.join(sorted_words)