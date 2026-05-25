def fractionToDecimal(numerator, denominator):
    if numerator == 0:
        return "0"
    
    result = ""
    if (numerator < 0) ^ (denominator < 0):
        result += "-"
    
    numerator, denominator = abs(numerator), abs(denominator)
    
    result += str(numerator // denominator)
    remainder = numerator % denominator
    
    if remainder == 0:
        return result
    
    result += "."
    remainder_map = {}
    
    while remainder != 0:
        if remainder in remainder_map:
            start = remainder_map[remainder]
            result = result[:start] + "(" + result[start:] + ")"
            break
        
        remainder_map[remainder] = len(result)
        remainder *= 10
        result += str(remainder // denominator)
        remainder %= denominator
    
    return result