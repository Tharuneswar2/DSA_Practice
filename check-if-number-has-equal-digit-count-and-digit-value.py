# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def digitCount(num):
    # Convert the number into a string to easily access each digit
    num_str = str(num)
    
    # Iterate over each character (digit) in the string
    for i, digit in enumerate(num_str):
        # If the digit is not equal to the count of the digit in the rest of the string, return False
        if int(digit) != num_str.count(str(i)):
            return False
            
    # If the loop completes without returning False, the number has equal digit count and digit value
    return True