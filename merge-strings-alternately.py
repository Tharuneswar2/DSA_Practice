def mergeAlternately(word1, word2):
    result = ""
    min_len = min(len(word1), len(word2))  # find the length of the shorter string
    
    # merge characters from both strings alternately
    for i in range(min_len):
        result += word1[i] + word2[i]
    
    # append the remaining characters from the longer string
    result += word1[min_len:] + word2[min_len:]
    
    return result