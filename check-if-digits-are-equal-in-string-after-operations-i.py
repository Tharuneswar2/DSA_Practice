# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def digitCount(s: str) -> bool:
    # Initialize a dictionary to store the frequency of each digit in the string
    freq = {}
    
    # Iterate over each character in the string
    for char in s:
        # If the character is already in the dictionary, increment its count
        if char in freq:
            freq[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            freq[char] = 1
    
    # Iterate over each character and its frequency in the dictionary
    for char, count in freq.items():
        # If the frequency of the character is not equal to the digit it represents, return False
        if int(char) != count:
            return False
    
    # If we have checked all characters and their frequencies, and haven't returned False, return True
    return True