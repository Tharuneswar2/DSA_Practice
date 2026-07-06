def freqAlphabets(s: str) -> str:
    # Initialize an empty string to store the result
    result = ""

    # Initialize an index to track the current position in the string
    i = 0

    # Loop through the string until we've processed all characters
    while i < len(s):
        # If the current character is '#', it means we have a 2-digit number
        if s[i] == '#':
            # Extract the 2-digit number and convert it to an integer
            num = int(s[i-2:i])
            # Convert the integer to a character and add it to the result
            result += chr(96 + num)
            # Move the index 3 positions forward to skip the 2-digit number and '#'
            i += 3
        else:
            # If the current character is not '#', it's a single digit number
            # Convert the digit to an integer and then to a character
            result += chr(96 + int(s[i]))
            # Move the index 1 position forward
            i += 1

    # Return the decrypted string
    return result