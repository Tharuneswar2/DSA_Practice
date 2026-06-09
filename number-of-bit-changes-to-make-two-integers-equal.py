def bitwiseComplement(N: int) -> int:
    # Calculate the number of bits in N
    bits = 0
    n = N
    while n:
        bits += 1
        n >>= 1
    
    # Create a mask with all bits set to 1 up to the number of bits in N
    mask = (1 << bits) - 1
    
    # XOR N with the mask to flip all bits
    return N ^ mask