# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def minPushes(word1, word2):
    # Initialize two pointers, one for each word
    i, j = 0, 0
    
    # Initialize the count of pushes
    pushes = 0
    
    # Traverse both words
    while i < len(word1) and j < len(word2):
        # If the current characters in both words are the same, increment both pointers
        if word1[i] == word2[j]:
            i += 1
            j += 1
        # If the current character in word1 is not the same as the current character in word2
        else:
            # Increment the pushes count by the difference between the current positions in both words
            pushes += abs(i - j)
            # Move the pointer of the word with the smaller current character to the next character
            if word1[i] < word2[j]:
                i += 1
            else:
                j += 1
                
    # Add the remaining characters in both words to the pushes count
    pushes += len(word1) - i
    pushes += len(word2) - j
    
    return pushes