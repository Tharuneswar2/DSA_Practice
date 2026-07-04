def odd_string_difference(words):
    # Calculate the difference between consecutive characters in the first word
    diff = [ord(words[0][i+1]) - ord(words[0][i]) for i in range(len(words[0]) - 1)]
    
    # Iterate over the rest of the words
    for word in words[1:]:
        # Calculate the difference between consecutive characters in the current word
        curr_diff = [ord(word[i+1]) - ord(word[i]) for i in range(len(word) - 1)]
        
        # If the difference is not the same as the first word, return the current word
        if curr_diff != diff:
            return word

# Test the function
print(odd_string_difference(["adc", "wzy", "abc"]))  # Output: "abc"