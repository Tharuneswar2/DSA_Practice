# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def areOccurrencesEqual(s: str) -> bool:
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
    expected_frequency = char_frequency[s[0]]
    
    # Iterate over the frequency of each character in the dictionary
    for frequency in char_frequency.values():
        # If any character has a different frequency than the expected frequency, return False
        if frequency != expected_frequency:
            return False
    
    # If all characters have the same frequency, return True
    return True