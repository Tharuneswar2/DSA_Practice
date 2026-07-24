# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def trim_trailing_vowels(s):
    # Define the set of vowels for efficient look-up
    vowels = set('aeiouAEIOU')
    
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over the input string from right to left
    for char in reversed(s):
        # If the character is not a vowel, add it to the result and break the loop
        if char not in vowels:
            result = char + result
            break
        # If the character is a vowel, add it to the result
        else:
            result = char + result
    
    # If the result is empty, it means the input string ended with a vowel, so return the original string
    if not result:
        return s
    # Otherwise, return the result
    else:
        return result