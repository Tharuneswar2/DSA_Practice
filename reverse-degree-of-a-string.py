# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def reverse_words(s):
    # Split the input string into a list of words
    words = s.split()
    
    # Initialize an empty list to store the reversed words
    reversed_words = []
    
    # Iterate over each word in the list of words
    for word in words:
        # Reverse the word and add it to the list of reversed words
        reversed_words.append(word[::-1])
    
    # Join the reversed words back into a string separated by spaces
    reversed_string = ' '.join(reversed_words)
    
    # Return the resulting string
    return reversed_string