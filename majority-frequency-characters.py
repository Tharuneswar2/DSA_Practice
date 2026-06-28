def majority_frequency_characters(s):
    # Create a dictionary to store the frequency of each character
    char_frequency = {}
    
    # Iterate over the string to count the frequency of each character
    for char in s:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    
    # Find the maximum frequency
    max_frequency = max(char_frequency.values())
    
    # Find the characters with the maximum frequency
    majority_chars = [char for char, frequency in char_frequency.items() if frequency == max_frequency]
    
    return majority_chars

# Test the function
print(majority_frequency_characters("abcde"))
print(majority_frequency_characters("aabbc"))
print(majority_frequency_characters("aaaaa"))