# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def is_fascinating(n):
    # Convert the number to a string to easily access each digit
    str_n = str(n)
    
    # Check if the number has 3 digits, a fascinating number must have 3 digits
    if len(str_n) != 3:
        return False
    
    # Initialize a set to store the digits of the number
    digits = set()
    
    # Iterate over each digit in the number
    for digit in str_n:
        # If the digit is already in the set, the number is not fascinating
        if digit in digits:
            return False
        # Add the digit to the set
        digits.add(digit)
    
    # Check if the number contains all digits from 1 to 9
    for i in range(1, 10):
        # If the number does not contain a digit, it's not fascinating
        if str(i) not in str_n and str(i) not in str(n*2) and str(i) not in str(n*3):
            return False
    
    # If the number passes all checks, it's fascinating
    return True

def check_fascinating():
    # Get the input number
    n = int(input())
    
    # Check if the number is fascinating
    if is_fascinating(n):
        print("Fascinating")
    else:
        print("Not Fascinating")

check_fascinating()