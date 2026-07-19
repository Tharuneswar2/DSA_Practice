# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def mergeAlternately(word1, word2):
    # Initialize an empty result string to store the merged string
    result = ""
    
    # Find the minimum length between the two input strings
    min_length = min(len(word1), len(word2))
    
    # Iterate over the range of the minimum length
    for i in range(min_length):
        # Append the character at the current index from the first string to the result
        result += word1[i]
        # Append the character at the current index from the second string to the result
        result += word2[i]
    
    # If the length of the first string is greater than the second string, append the remaining characters from the first string
    if len(word1) > len(word2):
        result += word1[min_length:]
    # If the length of the second string is greater than the first string, append the remaining characters from the second string
    elif len(word2) > len(word1):
        result += word2[min_length:]
    
    # Return the merged string
    return result