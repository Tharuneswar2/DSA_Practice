def remove_anagrams(words):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over each word in the input list
    for word in words:
        # Initialize a flag to check if the word is an anagram of the previous word
        is_anagram = False
        
        # If the result list is not empty, check if the current word is an anagram of the last word in the result list
        if result:
            # Sort the characters in the current word and the last word in the result list
            sorted_word = sorted(word)
            sorted_last_word = sorted(result[-1])
            
            # If the sorted characters are equal, the words are anagrams
            if sorted_word == sorted_last_word:
                is_anagram = True
        
        # If the word is not an anagram of the previous word, add it to the result list
        if not is_anagram:
            result.append(word)
    
    # Return the result list
    return result

# Test the function
words = ["abba", "baab", "abc", "cba", "abcd"]
print(remove_anagrams(words))