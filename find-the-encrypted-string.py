# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def encrypt_string(s):
    # Initialize an empty string to store the encrypted string
    encrypted_str = ""
    
    # Iterate over each character in the input string
    for i in range(len(s)):
        # If the character is at an even index, convert it to lowercase
        if i % 2 == 0:
            encrypted_str += s[i].lower()
        # If the character is at an odd index, convert it to uppercase
        else:
            encrypted_str += s[i].upper()
    
    # Return the encrypted string
    return encrypted_str