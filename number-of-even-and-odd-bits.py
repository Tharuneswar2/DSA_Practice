def count_even_odd_bits(n):
    # Initialize counters for even and odd bits
    even_bits = 0
    odd_bits = 0
    
    # Loop until n becomes 0
    while n:
        # Check the least significant bit of n
        # If it's 1, increment odd_bits, else increment even_bits
        if n & 1:
            odd_bits += 1
        else:
            even_bits += 1
        
        # Right shift n by 1 bit to move to the next bit
        n >>= 1
    
    # Return the counts of even and odd bits
    return even_bits, odd_bits

# Test the function
n = 5  # Binary representation: 101
even_bits, odd_bits = count_even_odd_bits(n)
print(f"Even bits: {even_bits}, Odd bits: {odd_bits}")