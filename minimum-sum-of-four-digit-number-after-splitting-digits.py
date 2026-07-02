def minimumSum(num):
    # Convert the number into a list of digits
    digits = [int(d) for d in str(num)]
    
    # Sort the digits in ascending order
    digits.sort()
    
    # Combine the smallest two digits and the largest two digits separately
    # This will result in the smallest possible sum
    return (digits[0] * 10 + digits[1]) + (digits[2] * 10 + digits[3])