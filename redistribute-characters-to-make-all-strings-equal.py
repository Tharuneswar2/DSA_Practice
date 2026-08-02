# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def makeEqual(words):
    # Create a dictionary to store the frequency of each character across all strings
    char_freq = {}
    for word in words:
        # Iterate over each character in the current string
        for char in word:
            # If the character is already in the dictionary, increment its count
            if char in char_freq:
                char_freq[char] += 1
            # If the character is not in the dictionary, add it with a count of 1
            else:
                char_freq[char] = 1
    
    # Calculate the number of strings
    num_strings = len(words)
    
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate over each character and its frequency in the dictionary
    for char, freq in char_freq.items():
        # If the frequency of the character is not divisible by the number of strings, return an empty string
        if freq % num_strings != 0:
            return ""
        # Otherwise, append the character to the result string the number of times it should appear in each string
        else:
            result += char * (freq // num_strings)
    
    # Return the result string
    return result