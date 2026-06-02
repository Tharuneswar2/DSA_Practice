def min_bit_flips(start, goal):
    # XOR operation will give us the bits that are different between start and goal
    xor_result = start ^ goal
    
    # Initialize count of bit flips
    count = 0
    
    # While there are still bits set in xor_result
    while xor_result:
        # Clear the least significant bit set in xor_result
        # This effectively counts the number of bits set in xor_result
        count += xor_result & 1
        # Right shift xor_result to move to the next bit
        xor_result >>= 1
    
    # Return the total count of bit flips
    return count