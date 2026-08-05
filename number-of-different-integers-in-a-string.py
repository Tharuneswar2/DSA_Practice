# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def numDifferentIntegers(word):
    # Initialize an empty set to store unique integers
    unique_integers = set()
    
    # Initialize an empty string to build the current integer
    current_integer = ""
    
    # Iterate over each character in the input string
    for char in word:
        # Check if the character is a digit
        if char.isdigit():
            # If the character is a digit, add it to the current integer
            current_integer += char
        else:
            # If the character is not a digit and the current integer is not empty
            if current_integer != "":
                # Add the current integer to the set of unique integers
                unique_integers.add(int(current_integer))
                # Reset the current integer
                current_integer = ""
    
    # After iterating over the entire string, check if the current integer is not empty
    if current_integer != "":
        # Add the current integer to the set of unique integers
        unique_integers.add(int(current_integer))
    
    # Return the number of unique integers
    return len(unique_integers)