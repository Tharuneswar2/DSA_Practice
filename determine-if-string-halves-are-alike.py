def halvesAreAlike(s: str) -> bool:
    # Convert the string to lowercase to handle case-insensitive comparison
    s = s.lower()
    
    # Calculate the middle index of the string
    mid = len(s) // 2
    
    # Split the string into two halves
    first_half = s[:mid]
    second_half = s[mid:]
    
    # Define the vowels in the English alphabet
    vowels = 'aeiou'
    
    # Initialize counters for vowels in each half
    first_half_vowels = 0
    second_half_vowels = 0
    
    # Count the vowels in the first half
    for char in first_half:
        if char in vowels:
            first_half_vowels += 1
    
    # Count the vowels in the second half
    for char in second_half:
        if char in vowels:
            second_half_vowels += 1
    
    # Return True if the number of vowels in each half is equal, False otherwise
    return first_half_vowels == second_half_vowels