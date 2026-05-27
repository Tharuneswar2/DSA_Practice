def find_words_containing_char(lst, char):
    # Initialize an empty list to store the words containing the character
    result = []
    
    # Iterate over each word in the input list
    for word in lst:
        # Check if the character is in the word
        if char in word:
            # If the character is found, append the word to the result list
            result.append(word)
    
    # Return the list of words containing the character
    return result

# Example usage:
words = ["apple", "banana", "cherry", "date", "elderberry"]
char = "e"
print(find_words_containing_char(words, char))