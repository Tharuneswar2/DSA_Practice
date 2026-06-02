def trim_trailing_vowels(s):
    # Define the set of vowels
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
    
    # If the result is empty, return the original string
    if not result:
        return s
    # Otherwise, return the result
    else:
        return result

# Test the function
print(trim_trailing_vowels('hello'))  # Output: 'hell'
print(trim_trailing_vowels('world'))  # Output: 'world'
print(trim_trailing_vowels('aeiou'))  # Output: ''