# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def hasTrailingZeros(n):
    # Initialize a variable to store the result of the bitwise OR operation
    bitwise_or = 0
    
    # Iterate over the range from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Perform a bitwise OR operation between the current number and the result so far
        bitwise_or |= i
    
    # Convert the result to binary and remove the '0b' prefix
    binary = bin(bitwise_or)[2:]
    
    # Check if the binary representation ends with a zero
    # If it does, return True; otherwise, return False
    return binary.endswith('0')