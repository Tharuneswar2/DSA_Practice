# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def percentage_letter(s, letter):
    # Convert the string to lowercase to handle case-insensitive comparison
    s = s.lower()
    # Convert the letter to lowercase to handle case-insensitive comparison
    letter = letter.lower()
    # Initialize a counter to store the count of the letter in the string
    count = 0
    # Iterate over each character in the string
    for char in s:
        # Check if the character is the same as the given letter
        if char == letter:
            # If it is, increment the counter
            count += 1
    # Calculate the percentage of the letter in the string
    # If the string is empty, return 0 to avoid division by zero error
    if len(s) == 0:
        return 0
    # Calculate the percentage and return it
    return (count / len(s)) * 100