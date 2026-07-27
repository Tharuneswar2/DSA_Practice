# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def repeatedCharacter(s):
    # Create an empty set to store characters we've seen so far
    seen = set()
    
    # Iterate over each character in the string
    for char in s:
        # If the character is already in the set, it's the first character to appear twice
        if char in seen:
            # Return the character
            return char
        # Otherwise, add the character to the set
        seen.add(char)