# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def smallest_number_with_all_set_bits(n):
    # Initialize the result variable to 0
    result = 0
    
    # Initialize the current bit position to 0
    bit_position = 0
    
    # Iterate over the range from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Left shift 1 by the current bit position to create a binary number with only the current bit set
        # Add this number to the result to set the current bit in the result
        result |= 1 << bit_position
        
        # Increment the bit position for the next iteration
        bit_position += 1
        
        # If the bit position is equal to the number of bits required to represent the number i in binary
        # Reset the bit position to 0 to start setting bits from the least significant bit again
        if bit_position == i.bit_length():
            bit_position = 0
    
    # Return the result
    return result