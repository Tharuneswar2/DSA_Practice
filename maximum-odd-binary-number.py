def maximum_odd_binary_number(n):
    # Convert the number to binary and remove the '0b' prefix
    binary = bin(n)[2:]
    
    # Find the first '0' from the right
    zero_index = len(binary) - 1 - binary[::-1].find('0')
    
    # If no '0' is found, return the number itself (it's already the maximum odd binary number)
    if zero_index == len(binary):
        return n
    
    # Flip the first '0' from the right to '1'
    binary = binary[:zero_index] + '1' + binary[zero_index + 1:]
    
    # Flip all '1's to the right of the flipped '0' to '0's
    binary = binary[:zero_index + 1] + '0' * (len(binary) - zero_index - 1)
    
    # Convert the binary string back to an integer
    return int(binary, 2)

# Test the function
print(maximum_odd_binary_number(10))  # Output: 9
print(maximum_odd_binary_number(7))   # Output: 7