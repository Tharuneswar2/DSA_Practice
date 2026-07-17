# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def secondHighest(self, s: str) -> int:
    # Initialize an empty set to store unique digits from the string
    digits = set()
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a digit
        if char.isdigit():
            # Add the digit to the set
            digits.add(int(char))
    
    # If there are less than 2 unique digits, return -1 as per the problem statement
    if len(digits) < 2:
        return -1
    
    # Remove the maximum digit from the set
    digits.remove(max(digits))
    
    # Return the maximum digit from the remaining set, which is the second highest digit
    return max(digits)