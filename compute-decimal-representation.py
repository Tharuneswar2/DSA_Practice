# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def fractionToDecimal(numerator, denominator):
    # Check if the result will be negative
    if (numerator < 0) ^ (denominator < 0):
        sign = "-"
    else:
        sign = ""
        
    # Convert both numbers to positive
    numerator, denominator = abs(numerator), abs(denominator)
    
    # Calculate the integer part
    integer_part = sign + str(numerator // denominator)
    
    # Calculate the remainder
    remainder = numerator % denominator
    
    # If the remainder is 0, return the integer part
    if remainder == 0:
        return integer_part
    
    # Initialize the decimal part and the dictionary to store the remainders
    decimal_part = ""
    remainders = {}
    
    # Calculate the decimal part
    while remainder != 0 and remainder not in remainders:
        remainders[remainder] = len(decimal_part)
        remainder *= 10
        decimal_part += str(remainder // denominator)
        remainder %= denominator
    
    # If the remainder is not 0, it means we have a repeating decimal
    if remainder != 0:
        start = remainders[remainder]
        decimal_part = decimal_part[:start] + "(" + decimal_part[start:] + ")"
    
    # Return the result
    return integer_part + "." + decimal_part