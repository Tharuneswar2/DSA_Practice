# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def find_words_containing_char(words, char):
    # Initialize an empty list to store the words containing the character
    result = []
    
    # Iterate over each word in the list of words
    for word in words:
        # Check if the character is present in the word
        if char in word:
            # If the character is present, append the word to the result list
            result.append(word)
    
    # Return the list of words containing the character
    return result

# Example usage:
words = ["apple", "banana", "cherry", "date", "elderberry"]
char = "e"
print(find_words_containing_char(words, char))