# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def countBits(n):
    # Initialize variables to store the count of even and odd bits
    even_bits = 0
    odd_bits = 0
    
    # Loop through all numbers from 0 to n (inclusive)
    for i in range(n + 1):
        # Convert the current number to binary and remove the '0b' prefix
        binary = bin(i)[2:]
        
        # Count the number of '1's in the binary representation (i.e., the number of odd bits)
        odd_bits += binary.count('1')
        
        # The number of even bits is the total number of bits minus the number of odd bits
        even_bits += len(binary) - binary.count('1')
    
    # Return the counts of even and odd bits as a list
    return [even_bits, odd_bits]