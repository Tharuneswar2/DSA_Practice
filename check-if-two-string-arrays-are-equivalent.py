# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def arrayStringsAreEqual(word1, word2):
    # Join all strings in word1 into a single string
    str1 = ''.join(word1)
    
    # Join all strings in word2 into a single string
    str2 = ''.join(word2)
    
    # Compare the two resulting strings
    # If they are equal, return True; otherwise, return False
    return str1 == str2