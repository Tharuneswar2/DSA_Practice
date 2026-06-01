def hex_to_base36(hex_string):
    # Convert hexadecimal to decimal
    decimal = int(hex_string, 16)
    
    # Initialize an empty string to store the base36 result
    base36 = ""
    
    # Define the base36 characters
    base36_chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    
    # Perform the conversion
    while decimal > 0:
        remainder = decimal % 36
        base36 = base36_chars[remainder] + base36
        decimal = decimal // 36
    
    return base36


def base36_to_hex(base36_string):
    # Define the base36 characters
    base36_chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    
    # Initialize the decimal value
    decimal = 0
    
    # Perform the conversion
    for i, char in enumerate(base36_string[::-1]):
        decimal += base36_chars.index(char) * (36 ** i)
    
    # Convert decimal to hexadecimal
    hex_string = hex(decimal)[2:]
    
    return hex_string


# Test the functions
hex_string = "1a2b3c"
base36_string = hex_to_base36(hex_string)
print(f"Hexadecimal {hex_string} is equal to base36 {base36_string}")

print(f"Base36 {base36_string} is equal to hexadecimal {base36_to_hex(base36_string)}")