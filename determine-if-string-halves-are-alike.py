# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def halvesAreAlike(s: str) -> bool:
    # Convert the string to lowercase to handle case-insensitive comparison
    s = s.lower()
    
    # Calculate the middle index of the string
    mid = len(s) // 2
    
    # Split the string into two halves
    first_half = s[:mid]
    second_half = s[mid + len(s) % 2:]  # Adjust the second half for odd-length strings
    
    # Initialize counters for vowels in each half
    vowels = 'aeiou'
    first_half_vowels = sum(1 for char in first_half if char in vowels)
    second_half_vowels = sum(1 for char in second_half if char in vowels)
    
    # Return True if the number of vowels in each half is equal, False otherwise
    return first_half_vowels == second_half_vowels