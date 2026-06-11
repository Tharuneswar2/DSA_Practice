def removeDigit(number: str, digit: str) -> str:
    # Find the first occurrence of the digit in the number
    idx = number.find(digit)
    
    # If the digit is not found, return the number as it is
    if idx == -1:
        return number
    
    # Remove the digit from the number
    new_number = number[:idx] + number[idx+1:]
    
    # If the new number is greater than the original number without the first occurrence of the digit,
    # return the new number
    if int(new_number) > int(number.replace(digit, '', 1)):
        return new_number
    
    # Otherwise, remove the digit from the rest of the number and return the result
    return max(new_number, number.replace(digit, '', 1))