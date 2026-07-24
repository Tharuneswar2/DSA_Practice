# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def areAllCharactersEqual(s):
    # Create a dictionary to store the frequency of each character in the string
    char_frequency = {}
    
    # Iterate over each character in the string
    for char in s:
        # If the character is already in the dictionary, increment its count
        if char in char_frequency:
            char_frequency[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            char_frequency[char] = 1
    
    # Get the frequency of the first character in the string
    # This will be used as a reference to compare with the frequency of other characters
    expected_frequency = char_frequency[s[0]]
    
    # Iterate over the frequency of each character in the dictionary
    for frequency in char_frequency.values():
        # If the frequency of any character is not equal to the expected frequency, return False
        if frequency != expected_frequency:
            return False
    
    # If the function has not returned False after checking all characters, return True
    return True