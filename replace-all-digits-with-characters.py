def replace_digits(s: str) -> str:
    # Create a dictionary mapping digits to their corresponding characters
    digit_map = {str(i): chr(96 + i) for i in range(1, 10)}
    digit_map['0'] = 'a'

    # Initialize an empty string to store the result
    result = ''

    # Iterate over each character in the input string
    for char in s:
        # If the character is a digit, replace