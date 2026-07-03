def first_letter_to_appear_twice(s):
    # Create a dictionary to store the frequency of each character
    char_freq = {}
    
    # Iterate over the string
    for char in s:
        # If the character is already in the dictionary, increment its count
        if char in char_freq:
            char_freq[char] += 1
            # If the count is 2, return the character
            if char_freq[char] == 2:
                return char
        # If the character is not in the dictionary, add it with a count of 1
        else:
            char_freq[char] = 1
    
    # If no character appears twice, return None
    return None

# Test the function
print(first_letter_to_appear_twice("abcda"))  # Output: 'a'
print(first_letter_to_appear_twice("abcde"))  # Output: None