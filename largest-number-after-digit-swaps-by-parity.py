# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def largestNumberAfterDigitSwapsByParity(num):
    # Convert the number into a list of digits for easier manipulation
    digits = [int(x) for x in str(num)]
    
    # Initialize two pointers, one for even indices and one for odd indices
    even_ptr, odd_ptr = 0, 1
    
    # Iterate over the digits
    while even_ptr < len(digits):
        # If the current even index digit is smaller than the next even index digit, swap them
        if even_ptr + 2 < len(digits) and digits[even_ptr] < digits[even_ptr + 2]:
            digits[even_ptr], digits[even_ptr + 2] = digits[even_ptr + 2], digits[even_ptr]
        
        # If the current odd index digit is smaller than the next odd index digit, swap them
        if odd_ptr + 2 < len(digits) and digits[odd_ptr] < digits[odd_ptr + 2]:
            digits[odd_ptr], digits[odd_ptr + 2] = digits[odd_ptr + 2], digits[odd_ptr]
        
        # Move the pointers two steps forward
        even_ptr += 2
        odd_ptr += 2
    
    # Convert the list of digits back into a number and return it
    return int(''.join(map(str, digits)))