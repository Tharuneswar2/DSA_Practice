# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def greatestLetter(s: str) -> str:
    # Create a set of the string to remove duplicate characters and have O(1) lookup time
    s_set = set(s)
    
    # Initialize the result as an empty string
    result = ""
    
    # Iterate over the set in reverse order to find the greatest letter
    for char in sorted(s_set, reverse=True):
        # Check if the character is in both lower and upper case
        if char.isupper() and char.lower() in s_set:
            # If it is, update the result and break the loop
            result = char
            break
        # If the character is in lower case, check if its upper case counterpart is in the set
        elif char.islower() and char.upper() in s_set:
            # If it is, update the result and break the loop
            result = char.upper()
            break
    
    # Return the result
    return result