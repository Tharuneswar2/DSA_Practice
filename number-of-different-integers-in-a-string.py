def numDifferentIntegers(word: str) -> int:
    # Initialize an empty set to store unique integers
    unique_integers = set()
    
    # Initialize an empty string to build the current integer
    current_integer = ""
    
    # Iterate over each character in the word
    for char in word:
        # If the character is a digit, add it to the current integer
        if char.isdigit():
            current_integer += char
        # If the character is not a digit and the current integer is not empty
        elif current_integer != "":
            # Add the current integer to the set of unique integers
            unique_integers.add(int(current_integer))
            # Reset the current integer
            current_integer = ""
    
    # If the word ends with a digit, add the last integer to the set
    if current_integer != "":
        unique_integers.add(int(current_integer))
    
    # Return the number of unique integers
    return len(unique_integers)