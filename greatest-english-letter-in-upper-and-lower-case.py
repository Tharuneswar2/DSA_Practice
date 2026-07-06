def greatestLetter(s: str) -> str:
    # Create a set of unique characters in the string for efficient lookups
    unique_chars = set(s)
    
    # Initialize the greatest letter to None
    greatest_letter = None
    
    # Iterate over the unique characters in descending order
    for char in sorted(unique_chars, reverse=True):
        # Check if both the uppercase and lowercase versions of the character exist in the string
        if char.isupper() and char.lower() in unique_chars:
            # If they do, update the greatest letter
            greatest_letter = char
            # We can break the loop since we've found the greatest letter
            break
    
    # Return the greatest letter
    return greatest_letter