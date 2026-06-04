def reverse_words(s):
    # Split the string into words
    words = s.split()
    
    # Initialize an empty list to store the reversed words
    reversed_words = []
    
    # Iterate over each word in the list of words
    for word in words:
        # Reverse the word and add it to the list of reversed words
        reversed_words.append(word[::-1])
    
    # Join the reversed words back into a string separated by spaces
    reversed_string = ' '.join(reversed_words)
    
    # Return the reversed string
    return reversed_string

def reverse_degree_of_string(s):
    # Call the function to reverse the words in the string
    reversed_string = reverse_words(s)
    
    # Return the reversed string
    return reversed_string

# Test the function
print(reverse_degree_of_string("Hello World"))