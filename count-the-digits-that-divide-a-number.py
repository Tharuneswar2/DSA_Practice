# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def findDigits(n):
    # Convert the number into a string to easily access each digit
    str_n = str(n)
    
    # Initialize a counter variable to store the count of digits that divide the number
    count = 0
    
    # Iterate over each character (digit) in the string
    for digit in str_n:
        # Convert the character back into an integer
        int_digit = int(digit)
        
        # Check if the digit is non-zero (to avoid division by zero error) and if it divides the number
        if int_digit != 0 and n % int_digit == 0:
            # If the digit divides the number, increment the counter
            count += 1
    
    # Return the count of digits that divide the number
    return count