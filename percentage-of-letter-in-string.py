def percentage_letter_in_string(s, letter):
    # Convert the string to lowercase to handle case-insensitive comparison
    s = s.lower()
    letter = letter.lower()

    # Initialize a counter to store the count of the given letter
    count = 0

    # Iterate over each character in the string
    for char in s:
        # Check if the character matches the given letter
        if char == letter:
            # Increment the counter if a match is found
            count += 1

    # Calculate the percentage of the given letter in the string
    percentage = (count / len(s)) * 100

    # Return the calculated percentage
    return percentage

# Example usage
s = "Hello World"
letter = "l"
print(percentage_letter_in_string(s, letter))