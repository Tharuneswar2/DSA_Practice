def stringMatching(words):
    # Sort the list of words by their lengths in ascending order
    words.sort(key=len)
    
    # Initialize an empty list to store the matched words
    matched_words = []
    
    # Iterate over each word in the sorted list
    for i in range(len(words)):
        # Iterate over the remaining words in the list
        for j in range(i + 1, len(words)):
            # Check if the current word is a substring of the next word
            if words[i] in words[j]:
                # If it is, add it to the list of matched words
                matched_words.append(words[i])
                # Break the inner loop to avoid duplicate matches
                break
    
    # Return the list of matched words
    return matched_words

# Example usage:
words = ["mass","as","hero","superhero"]
print(stringMatching(words))  # Output: ["as", "hero"]