# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def count_bit_changes(a, b):
    # Use the XOR operator (^) to find the bits that are different between a and b
    # The XOR operator returns 1 for each position where the corresponding bits of a and b are different
    different_bits = a ^ b
    
    # Initialize a variable to store the count of different bits
    count = 0
    
    # Loop until there are no more bits to check (i.e., different_bits becomes 0)
    while different_bits:
        # Use the bitwise AND operator (&) with 1 to check the least significant bit of different_bits
        # If the least significant bit is 1, it means there is a different bit at this position
        count += different_bits & 1
        
        # Right shift different_bits by 1 to move to the next bit
        different_bits >>= 1
    
    # Return the count of different bits
    return count