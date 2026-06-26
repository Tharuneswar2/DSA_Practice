def reversePrefix(word, ch):
    # Find the index of the character in the word
    idx = word.find(ch)
    
    # If the character is not found, return the word as it is
    if idx == -1:
        return word
    
    # Reverse the prefix of the word up to the index of the character
    prefix = word[:idx+1][::-1]
    
    # Return the reversed prefix concatenated with the rest of the word
    return prefix + word[idx+1:]

# Test the function
print(reversePrefix("abcdefd", "d"))  # Output: "dcbaefd"