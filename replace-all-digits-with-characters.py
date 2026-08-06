# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def replace_digits(s: str) -> str:
    # Initialize an empty string to store the result
    result = ""

    # Iterate over each character in the input string
    for char in s:
        # Check if the character is a digit
        if char.isdigit():
            # Convert the digit to its corresponding character (a for 0, b for 1, ..., z for 25)
            # The ASCII value of 'a' is 97, so we add the digit value to 97 to get the ASCII value of the corresponding character
            result += chr(int(char) + 97)
        else:
            # If the character is not a digit, just append it to the result
            result += char

    # Return the resulting string
    return result