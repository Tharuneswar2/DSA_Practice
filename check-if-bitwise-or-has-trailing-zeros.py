def has_trailing_zeros(n, m):
    # Calculate the bitwise OR of n and m
    bitwise_or = n | m
    
    # Convert the bitwise OR to binary and remove the '0b' prefix
    binary = bin(bitwise_or)[2:]
    
    # Check if the binary representation has trailing zeros
    # This is done by checking if the binary representation is a multiple of 2^i for any i > 0
    # We can do this by checking if the binary representation ends with a '0'
    # However, this approach is not efficient for large numbers
    # A more efficient approach is to check if the bitwise OR is a multiple of 2^i for any i > 0
    # We can do this by checking if the bitwise OR is divisible by 2
    return bitwise_or % 2 == 0

# Alternatively, we can use the following approach
def has_trailing_zeros_alternative(n, m):
    # Calculate the bitwise OR of n and m
    bitwise_or = n | m
    
    # Check if the bitwise OR is divisible by 2
    # If it is, then it has trailing zeros
    return bitwise_or % 2 == 0

# Another approach is to use bitwise operations
def has_trailing_zeros_bitwise(n, m):
    # Calculate the bitwise OR of n and m
    bitwise_or = n | m
    
    # Check if the bitwise OR has trailing zeros
    # We can do this by checking if the bitwise OR is divisible by 2
    # We can use the bitwise AND operator to check this
    # If the bitwise OR is divisible by 2, then the bitwise AND of the bitwise OR and 1 will be 0
    return (bitwise_or & 1) == 0