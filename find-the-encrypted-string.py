def encrypt_string(s):
    # Initialize an empty string to store the encrypted string
    encrypted_str = ""

    # Iterate over each character in the input string
    for char in s:
        # Check if the character is an alphabet
        if char.isalpha():
            # Calculate the ASCII value of the encrypted character
            # 'a' and 'A' have ASCII values 97 and 65 respectively
            # We subtract the ASCII value of 'a' or 'A' to get a value between 0 and 25
            # Then we add 1 to shift the character one position forward in the alphabet
            # Finally, we add the ASCII value of 'a' or 'A' back to get the ASCII value of the encrypted character
            if char.islower():
                encrypted_char = chr((ord(char) - 97 + 1) % 26 + 97)
            else:
                encrypted_char = chr((ord(char) - 65 + 1) % 26 + 65)
            # Append the encrypted character to the encrypted string
            encrypted_str += encrypted_char
        else:
            # If the character is not an alphabet, append it as it is to the encrypted string
            encrypted_str += char

    # Return the encrypted string
    return encrypted_str

# Test the function
print(encrypt_string("Hello, World!"))