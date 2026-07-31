# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def maximumOddBinaryNumber(n):
    # Convert the number to binary and remove the '0b' prefix that Python adds
    binary = bin(n)[2:]
    
    # Find the first occurrence of '0' from the right
    # This is because we want to replace the rightmost '0' with '1' to make it odd
    rightmost_zero = binary.rfind('0')
    
    # If no '0' is found, it means the number is already odd
    # In this case, we simply return the number as it is
    if rightmost_zero == -1:
        return n
    
    # Replace the rightmost '0' with '1'
    # This will make the number odd
    binary = binary[:rightmost_zero] + '1' + binary[rightmost_zero + 1:]
    
    # Convert the binary string back to an integer
    result = int(binary, 2)
    
    return result