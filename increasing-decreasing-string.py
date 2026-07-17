# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def sortString(s: str) -> str:
    # Create a dictionary to store the frequency of each character in the string
    freq = {}
    for char in s:
        # If the character is already in the dictionary, increment its count
        if char in freq:
            freq[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            freq[char] = 1
    
    # Initialize an empty string to store the result
    result = ''
    # Continue the process until all characters have been added to the result
    while len(result) < len(s):
        # First, add all characters in ascending order
        for char in sorted(freq.keys()):
            # If the character's frequency is greater than 0, add it to the result and decrement its frequency
            if freq[char] > 0:
                result += char
                freq[char] -= 1
        # Then, add all characters in descending order
        for char in sorted(freq.keys(), reverse=True):
            # If the character's frequency is greater than 0, add it to the result and decrement its frequency
            if freq[char] > 0:
                result += char
                freq[char] -= 1
    
    # Return the result
    return result